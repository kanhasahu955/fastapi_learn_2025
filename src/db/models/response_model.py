from typing import Dict,Optional
from pydantic import BaseModel

class SchemalessResponse(BaseModel):
    response: Dict = {}
    status_code: int = 200
    message: Optional[str] = "Request Processed"