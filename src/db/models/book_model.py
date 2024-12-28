from datetime import datetime
from pydantic import BaseModel
import uuid

class Book(BaseModel):
    uid: uuid.UUID 
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    created_at:datetime
    updated_at:datetime
    
class CreateBookModel(BaseModel):
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    
class UpdateBookModel(BaseModel):
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str