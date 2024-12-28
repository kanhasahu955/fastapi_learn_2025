from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc

from src.db.schemas.book_schema import Book
from src.db.models.book_model import CreateBookModel, UpdateBookModel
from src.db.models.response_model import SchemalessResponse

class BookService:
    async def get_all_books(self,session:AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.execute(statement)
        response = SchemalessResponse(
            response=dict(
                success=True,
                data=result.all()
            ),
            message="user created successfully"
        )
        return JSONResponse(jsonable_encoder(response))

            
    async def get_book(self,book_id:int,session:AsyncSession):
        pass
    
    async def create_book(self,book_data:CreateBookModel,session:AsyncSession):
        book_data_dict = book_data.model_dump();
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
    
    async def update_book(self,book_data:UpdateBookModel,session:AsyncSession):
        pass
    
    async def delete_book(self,book_id:int,session:AsyncSession):
        pass
    
    