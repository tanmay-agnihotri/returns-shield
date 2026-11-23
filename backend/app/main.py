import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import fraud, returns, marketplace, search

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShieldMart API", version="2.0.0")

# Comma-separated list of allowed frontend origins. Override with the
# CORS_ORIGINS env var (e.g. on Render) instead of allowing every origin.
DEFAULT_CORS_ORIGINS = (
    "http://localhost:5173,http://localhost:5174,http://localhost:3000,"
    "https://returndetection-ks5p.vercel.app"
)
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", DEFAULT_CORS_ORIGINS).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fraud.router)
app.include_router(returns.router)
app.include_router(marketplace.router)
app.include_router(search.router)


@app.get("/")
def root():
    return {
        "app": "ShieldMart",
        "version": "2.0.0",
        "tagline": "AI-verified used goods marketplace",
        "status": "running"
    }