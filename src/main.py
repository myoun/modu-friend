from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config import Settings

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print(settings)
    yield

    # Shutdown

    return

app = FastAPI(lifespan=lifespan)