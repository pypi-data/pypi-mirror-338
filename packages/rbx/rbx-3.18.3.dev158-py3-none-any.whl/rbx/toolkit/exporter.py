import logging

from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route

from . import Options, run

config = Config()
logging.basicConfig(level=config("LOG_LEVEL", default="INFO"))


async def handler(request):
    payload = await request.json()

    errors = []
    for param in ("url", "width", "height", "format", "name"):
        if param not in payload.keys():
            errors.append(f"Missing required '{param}' parameter")

    if payload.get("format") == "video" and "duration" not in payload.keys():
        errors.append("Missing required 'duration' parameter")

    if errors:
        return JSONResponse({"errors": errors}, status_code=400)

    ext = "mp4" if payload["format"] == "video" else "png"
    filename = f"{payload['name']}.{ext}"
    project_id = config("GOOGLE_CLOUD_PROJECT", default="dev-platform-eu")
    output = f"gs://{project_id}.appspot.com/toolkit/exports/"

    await run(
        options=Options(
            url=payload["url"],
            width=payload["width"],
            height=payload["height"],
            format=payload["format"],
            duration=int(payload.get("duration", 0)),
            output=output,
            filename=filename,
        )
    )

    return JSONResponse({"path": f"{output}{filename}"})


def create_app() -> Starlette:
    return Starlette(
        routes=[
            Route("/", endpoint=handler, methods=["POST"]),
        ]
    )
