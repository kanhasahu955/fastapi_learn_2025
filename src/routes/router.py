from fastapi import APIRouter

from src.routes.book_routes import book_router

api_router = APIRouter()

api_router.include_router(book_router,prefix='/book',tags=['Book'])