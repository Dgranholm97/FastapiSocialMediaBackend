from typing import Optional, List, TYPE_CHECKING   

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

DateTime = Optional[datetime]

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .post import Post  # noqa: F401
    
class LikeBase(SQLModel):
    user_id: int  = Field(index=True, foreign_key="user.id")
    post_id: int  = Field(index=True, foreign_key="post.id")

class Like(LikeBase, table=True):  
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: DateTime = Field(default_factory=datetime.utcnow)
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
    post: Post = Relationship(back_populates="likes")
    owner: User = Relationship(back_populates="likes")

class LikeRead(LikeBase, table=True):  
    id: int 
    created_at: DateTime 
    updated_at: DateTime
    post: Post 
    owner: User

class LikeCreate(LikeBase):
    pass

class LikeUpdate(SQLModel):
    pass