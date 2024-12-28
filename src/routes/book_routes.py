from fastapi import APIRouter,Depends,status
from typing import List
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.db.models.book_model import Book
from src.services.book_services import BookService

book_router = APIRouter()
book_service = BookService()

@book_router.get('/get_all',status_code=status.HTTP_200_OK,response_model=List[Book])
async def get_all(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post('/create',status_code=status.HTTP_201_CREATED,response_model=Book)
async def create_book(book_data:Book,session:AsyncSession = Depends(get_session))->dict:
    new_book = await book_service.create_book(book_data,session)
    return new_book

@book_router.patch('/update',status_code=status.HTTP_200_OK,response_model=Book)
async def update_book(book_data:Book,session:AsyncSession = Depends(get_session))->dict:
    new_book = await book_service.create_book(book_data,session)
    return new_book

@book_router.delete('/delete',status_code=status.HTTP_200_OK,response_model=Book)
async def update_book(book_data:Book,session:AsyncSession = Depends(get_session))->dict:
    new_book = await book_service.create_book(book_data,session)
    return new_book

@book_router.get('/get',status_code=status.HTTP_200_OK,response_model=Book)
async def update_book(book_data:Book,session:AsyncSession = Depends(get_session))->dict:
    new_book = await book_service.create_book(book_data,session)
    return new_book

