import datetime
import logging
import os
import signal
import subprocess
import time
import uuid

from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)


def get_free_display(base=99, max_tries=100):
    for i in range(max_tries):
        display = f":{base + i}"
        if not os.path.exists(f"/tmp/.X{base + i}-lock"):
            return display

    raise RuntimeError("No free display found")


class RecordingSession:
    def __init__(self, dirname, width, height):
        self.display = get_free_display()
        self.dirname = dirname
        self.width = width
        self.height = height
        self.resolution = f"{self.width}x{self.height}"
        self.session_id = str(uuid.uuid4())[:8]
        self.sink_name = f"rec_sink_{self.session_id}"
        self.pulse_dir = f"{dirname}/pulseaudio"
        self.pulse_socket = os.path.join(self.pulse_dir, "pulse-socket")
        self.proc = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        logger.debug("Stopping processes...")

        # PulseAudio needs to be terminated via the kill command.
        subprocess.Popen(
            ["pulseaudio", "--kill"],
            env={
                "PULSE_SERVER": f"unix:{self.pulse_socket}",
                "XDG_RUNTIME_DIR": self.pulse_dir,
            },
        )

        for proc in reversed(self.proc):
            if proc and proc.poll() is None:
                try:
                    proc.send_signal(signal.SIGINT)
                    proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    proc.kill()

    def start_xvfb(self):
        logger.debug(f"Starting Xvfb [{self.display}]...")
        # fmt: off
        self.proc.append(
            subprocess.Popen(
                [
                    "Xvfb", self.display, "-screen", "0", f"{self.resolution}x24",
                    # These options are needed when running in a container
                    "-ac", "-nolisten", "tcp", "-nolisten", "unix",
                ]
            )
        )
        # fmt: on
        time.sleep(1)

        logger.debug(f"Starting unclutter [{self.display}]...")
        self.proc.append(
            subprocess.Popen(
                ["unclutter", "-idle", "0"],
                env={"DISPLAY": self.display},
            )
        )

    def start_pulseaudio(self):
        logger.debug(f"Starting PulseAudio [{self.pulse_dir}.{self.sink_name}]...")
        os.makedirs(self.pulse_dir, exist_ok=True)
        os.chmod(self.pulse_dir, 0o700)  # PulseAudio requires strict permissions

        subprocess.Popen(
            [
                "pulseaudio",
                "--start",
                "--disable-shm",
                "--exit-idle-time=300",
                f"--load=module-native-protocol-unix socket={self.pulse_socket}",
                f"--load=module-null-sink sink_name={self.sink_name}"
                f" sink_properties=device.description={self.sink_name}",
            ],
            env={
                "DISPLAY": self.display,
                "PULSE_NO_SIMD": 1,
                "XDG_RUNTIME_DIR": self.pulse_dir,
            },
        )
        time.sleep(2)

    def start_ffmpeg(self, duration, output_path):
        logger.debug(f"Starting FFmpeg recording [{self.display}:{self.sink_name}]...")
        # fmt: off
        self.proc.append(
            subprocess.Popen(
                [
                    "ffmpeg", "-y",
                    "-t", str(duration),
                    "-video_size", self.resolution,
                    "-f", "x11grab",
                    "-i", f"{self.display}.0",
                    "-f", "pulse",
                    "-i", f"{self.sink_name}.monitor",
                    "-c:v", "libx264",
                    "-preset", "slow",
                    "-crf", "8",
                    "-pix_fmt", "yuv420p",
                    "-c:a", "aac",
                    "-b:a", "256k",
                    "-movflags",
                    "+faststart",
                    output_path,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
                env={
                    "PULSE_SERVER": f"unix:{self.pulse_socket}",
                    "XDG_RUNTIME_DIR": self.pulse_dir,
                },
            )
        )
        # fmt: on

    async def capture(self, url, duration, output_path):
        self.start_xvfb()
        self.start_pulseaudio()

        async with async_playwright() as p:
            logger.debug(
                f"Capturing Chromium session [{self.display}:{self.sink_name}]..."
            )
            context = await p.chromium.launch_persistent_context(
                user_data_dir=f"{self.dirname}/user-data",
                headless=False,
                channel="chrome",
                args=[
                    "--no-sandbox",
                    "--disable-gpu",
                    "--disable-software-rasterizer",
                    f"--display={self.display}",
                    "--autoplay-policy=no-user-gesture-required",
                    "--use-fake-ui-for-media-stream",
                    f"--alsa-output-device={self.sink_name}",
                    "--start-fullscreen",
                    "--window-position=0,0",
                    f"--window-size={self.width},{self.height}",
                ],
                ignore_default_args=["--enable-automation"],
                no_viewport=True,
                env={
                    "PULSE_SERVER": f"unix:{self.pulse_socket}",
                    "XDG_RUNTIME_DIR": self.pulse_dir,
                },
            )
            page = await context.new_page()
            await page.goto(url, wait_until="commit")

            logger.info(
                f"Recording session [{self.display}:{self.sink_name}] for {duration}ms"
            )

            self.start_ffmpeg(duration, output_path)

            await page.wait_for_timeout(duration)  # Wait for the duration
            await context.close()


async def record(
    dirname: str, filename: str, duration: int, height: int, url: str, width: int
) -> None:
    async with RecordingSession(dirname, width, height) as session:
        await session.capture(url, duration, filename)


async def screenshot(filename: str, height: int, url: str, width: int) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": width, "height": height})
        await page.goto(url, wait_until="networkidle")
        await page.screenshot(path=filename)
        await browser.close()


def to_ms(timedelta: datetime.timedelta) -> int:
    return round(1000 * timedelta.total_seconds())
