from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello() -> dict[str, str]:
    return {"message": "Привет из FastAPI"}

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

# Все остальные пути → отдаём index.html
@app.get("/{full_path:path}")
def serve_vue(full_path: str, request: Request) -> FileResponse:
    return FileResponse("frontend/dist/index.html")
