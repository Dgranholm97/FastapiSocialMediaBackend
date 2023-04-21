from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api.api import api_router
from .db import create_db_and_tables

app = FastAPI()

# Set all CORS enabled origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api')

@app.on_event("startup")
def on_startup():
    create_db_and_tables()