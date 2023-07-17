from typing import List

from pydantic import BaseModel


class InsertAccountRequestDto(BaseModel):
    email: str
    cellphones: List[str]
