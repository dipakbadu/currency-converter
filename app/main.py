from fastapi import FastAPI
from app.routes.currency import router as currency_router

app = FastAPI()

app.include_router(currency_router, prefix="/api")
