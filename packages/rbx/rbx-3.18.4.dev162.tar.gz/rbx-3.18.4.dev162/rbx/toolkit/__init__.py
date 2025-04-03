__all__ = ["Options", "run"]

import logging
import tempfile
from pathlib import Path
from typing import NamedTuple, Optional

from .browser import record, screenshot
from .utils import upload

logger = logging.getLogger(__name__)


class Options(NamedTuple):
    url: str
    width: int
    height: int
    format: str
    duration: Optional[int] = 0
    path: Optional[str] = "/tmp"
    output: Optional[str] = "."
    filename: Optional[str] = None


def filename(output, filename):
    if output.startswith("s3://"):
        return "s3://" + str(Path(output[5:]) / filename)
    elif output.startswith("gs://"):
        return "gs://" + str(Path(output[5:]) / filename)
    return str(Path(output) / filename)


async def capture(filename: str, options: Options, path: Path) -> None:
    await record(
        dirname=str(path),
        filename=str(path / filename),
        duration=options.duration,
        height=options.height,
        url=options.url,
        width=options.width,
    )


async def screengrab(filename: str, options: Options, path: Path) -> None:
    await screenshot(
        filename=str(path / filename),
        height=options.height,
        url=options.url,
        width=options.width,
    )


async def run(options: Options) -> None:
    with tempfile.TemporaryDirectory(dir=options.path) as dirname:
        path = Path(dirname)
        logger.debug(f"Working directory: '{path}'")
        if options.format == "video":
            asset = options.filename or "video.mp4"
            output = filename(options.output, asset)
            if options.duration:
                logger.info(
                    f"Capturing '{options.url}' [{options.width}x{options.height}]"
                    f" for {options.duration}ms to '{output}'",
                )
            else:
                logger.info(
                    f"Capturing '{options.url}' [{options.width}x{options.height}] to '{output}'",
                )
            await capture(filename=asset, options=options, path=path)
        else:
            asset = options.filename or "screenshot.png"
            output = filename(options.output, asset)
            logger.info(
                f"Taking screenshot of '{options.url}' [{options.width}x{options.height}]"
                f" to '{output}'"
            )
            await screengrab(filename=asset, options=options, path=path)

        upload(path / asset, output)
