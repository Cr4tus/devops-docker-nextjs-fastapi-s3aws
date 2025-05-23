import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.qr import router as qr_router
from configs.constants import (
    DEFAULT_LOG_MESSAGE_FORMAT,
    ALLOWED_ORIGINS, ALLOWED_METHODS, ALLOWED_HEADERS
)


logging.basicConfig(level=logging.INFO, format=DEFAULT_LOG_MESSAGE_FORMAT)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=ALLOWED_METHODS,
    allow_headers=ALLOWED_HEADERS
)

app.include_router(qr_router)
