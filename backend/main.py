from fastapi import FastAPI

from core.config import settings

# app = FastAPI(title="Jobboard", version="0.1.0",)
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION,)


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
