from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class BookModel(BaseModel):
    title:str
    author:str

@app.post('/create_book')
async def create_book(book_details:BookModel)->dict:
    return{
        "title":book_details.title,
        "author":book_details.author
    }    