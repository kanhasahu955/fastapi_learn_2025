from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# simple get request
@app.get('/')
async def get_request():
    return {"message":"hello world"}

# path parameters
@app.get('/name/{name}')
async def get_name(name:str)->dict:
    return {"name":name}

# query parameters
@app.get('/query_params')
async def get_query_aprams(name:Optional[str] = 'User',age:Optional[int] = 10)->dict:
    return {"name":name,"age":age}

# getting headers values
@app.get('/headers',status_code=500)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    
    return request_headers
    

