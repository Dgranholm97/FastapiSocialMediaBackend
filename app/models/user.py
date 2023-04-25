from typing import Optional, List, TYPE_CHECKING 

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

from app.db import Base

DateTime = Optional[datetime]

if TYPE_CHECKING:
    from .post import Post  # noqa: F401
    from .like import Like  # noqa: F401
    from .comment import Comment  # noqa: F401
    
    
    
class UserBase(SQLModel):
    username: str
    
    email: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile_image: Optional[str] = None
   
class User(UserBase, table=True):  
    id: Optional[int] = Field(default=None, primary_key=True)  
    hashed_password: str
    created_at: DateTime = Field(default_factory=datetime.utcnow)
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    
    following: List["User"] = Relationship(back_populates="owner")#The back populate might need to be switched with followers
    followers: List["User"] = Relationship(back_populates="following")
    posts: List["Post"] = Relationship(back_populates="owner")
    likes: List["Like"] = Relationship(back_populates="owner")
    comments: List["Comment"] = Relationship(back_populates="owner")
    
class UserRead(UserBase):
    id: int
    created_at: DateTime
    updated_at: DateTime
    
class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    id:int