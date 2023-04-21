from typing import Optional, List, TYPE_CHECKING   

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

DateTime = Optional[datetime]

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .comment import Comment  # noqa: F401
    from .like import Like  # noqa: F401
    
class PostBase(SQLModel):
    user_id: int  = Field(index=True, foreign_key="user.id")
    text: str
    image_url: Optional[str] = None

    
class Post(PostBase, table=True):  
    id: Optional[int] = Field(default=None, primary_key=True)  
    created_at: DateTime = Field(default_factory=datetime.utcnow)
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
    owner: User = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")
    likes: List["Like"] = Relationship(back_populates="post")
    
class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    created_at: DateTime
    updated_at: DateTime
    owner: User

class PostUpdate(SQLModel):
    text: str
    image_url: Optional[str] = None