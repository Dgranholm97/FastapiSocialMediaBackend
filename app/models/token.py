from typing import Optional

#from pydantic import BaseModel

from sqlmodel import SQLModel

class Token(SQLModel):
    access_token: str
    token_type: str


class TokenPayload(SQLModel):
    sub: Optional[int] = None
