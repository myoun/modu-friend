from fastapi import FastAPI
from contextlib import asynccontextmanager
from .config import Settings

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    
    yield

    # Shutdown

    return

app = FastAPI(lifespan=lifespan)