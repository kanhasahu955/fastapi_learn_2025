import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.routes.router import api_router

version = 'v1'

@asynccontextmanager
async def lifespan(app:FastAPI):
    print(f'server is starting....')
    await init_db()
    yield
    print(f'server is stopped!')

app = FastAPI(
    title="FastAPI learn",
    description='FastAPI learning project',
    version='1.0',
    lifespan=lifespan
)
    
app.include_router(api_router,prefix=f'/api/{version}')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

