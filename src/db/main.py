from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.config import Config

# async_engine = AsyncEngine(
#     create_engine(
#     url  = Config.LOCAL_DATABASE_URL,
#     echo = True    ,
#     future=True
# ))

def get_engine():
    return create_async_engine(Config.LOCAL_DATABASE_URL, echo=True, future=True)
        

async def init_db():
    async with get_engine().begin() as conn:
        from src.db.schemas.book_schema import Book
        await conn.run_sync(Book.metadata.create_all)
        

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        get_engine(), class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

# async def get_session()->AsyncSession:
    
#     async_session = sessionmaker(
#         bind = async_engine,
#         class_ = AsyncSession,
#         expire_on_commit=False
#     )
    
#     async with async_session() as session:
#         yield session
        