from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import engine, Base
from app.routes.task_route import router
from scheduler import start_scheduler

# Create tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    start_scheduler()
    yield
    # Shutdown (optional for now)


# app entry point
app = FastAPI(lifespan=lifespan)

# Include routes
app.include_router(router)