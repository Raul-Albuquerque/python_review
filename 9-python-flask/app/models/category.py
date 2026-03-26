from pydantic import BaseModel
from typing import Optional


class Category(BaseModel):
    nome: str
    description: Optional[str] = None
