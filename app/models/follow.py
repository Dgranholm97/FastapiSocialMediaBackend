from typing import Optional, List, TYPE_CHECKING  

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

DateTime = Optional[datetime]

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    
class FollowBase(SQLModel):
    user_id: int  = Field(index=True, foreign_key="user.id")
    following_id: int  = Field(index=True, foreign_key="user.id")
           
class Follow(FollowBase, table=True):#This could also be simplified into a link table
    '''The follow object is owner bio the person who is following another user
    so if john is following jane then john is the owner and jane is the following'''  
    id: Optional[int] = Field(default=None, primary_key=True)  
    created_at: DateTime = Field(default_factory=datetime.utcnow) 
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
    owner: User = Relationship(back_populates="followers")
    following: User = Relationship(back_populates="followers")
    
class FollowRead(FollowBase):
    id:int
    created_at: DateTime
    update_at: DateTime
    
class FollowCreate(FollowBase):
    pass

class FollowUpdate(FollowBase):
    id:int