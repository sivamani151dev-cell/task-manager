from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, tasks
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple task manager backend API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {
        "message": "Welcome to Task Manager API! ✅",
        "docs": "http://localhost:8000/docs"
    }