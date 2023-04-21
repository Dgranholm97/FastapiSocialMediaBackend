from typing import Optional, List, TYPE_CHECKING   

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

DateTime = Optional[datetime]

if TYPE_CHECKING:
    from .post import Post  # noqa: F401
    from .user import User  # noqa: F401
    
    
class CommentBase(SQLModel):
    user_id: int  = Field(index=True, foreign_key="user.id")
    post_id: int  = Field(index=True, foreign_key="post.id")
    text: str

class Comment(CommentBase, table=True):  
    id: Optional[int] = Field(default=None, primary_key=True)
      
    created_at: Optional[DateTime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[DateTime] = Field(default_factory=datetime.utcnow)
    
    owner: User = Relationship(back_populates="comments")
    post: Post = Relationship(back_populates="comments")
    
class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: DateTime = Field(default_factory=datetime.utcnow)
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
class CommentUpdate(SQLModel):
    text:str
