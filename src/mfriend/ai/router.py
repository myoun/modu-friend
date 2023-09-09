from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.auth import schemas, crud, exceptions
from mfriend.openapi import OpenApiTags

router = APIRouter(
    prefix="/api/auth",
    tags=[OpenApiTags.AI]
)

