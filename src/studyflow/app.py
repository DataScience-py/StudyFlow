"""Create a fastapi application."""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_PATH = Path(__file__).parent.parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: deleate test method
@app.get("/api/hello")
def hello() -> dict[str, str]:
    """Hello router.

    Returns
    -------
        dict[str, str]: message
    """
    return {"message": "Привет из FastAPI"}


app.mount(
    "/assets",
    StaticFiles(directory=BASE_PATH / "frontend" / "dist" / "assets"),
    name="assets",
)


@app.get("/{full_path:path}")
def serve_vue(full_path: str, request: Request) -> FileResponse:  # noqa: ARG001
    """Serve the vue file.

    Args:
        full_path (str): [description]
        request (Request): [description]

    Returns
    -------
        FileResponse: [description]
    """
    return FileResponse("frontend/dist/index.html")
