"""Start server."""

from uvicorn import run

if __name__ == "__main__":
    # Run only for test, and developing
    run(app="studyflow.app:app", host="127.0.0.1", port=8000, reload=True)
