from typing import Optional, List   

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

DateTime = Optional[datetime]

class UserBase(SQLModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile_image: Optional[str] = None
   
class User(UserBase, table=True):  
    id: Optional[int] = Field(default=None, primary_key=True)  

    created_at: DateTime = Field(default_factory=datetime.utcnow)
    updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
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
    pass

class UserUpdate(UserBase):
    id:int
      
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
# class FollowLinkTable(SQLModel, table=True):
#     '''The follow object is owner bio the person who is following another user
#     so if john is following jane then john is the owner and jane is the following'''  
#     user_id: int  = Field(index=True, foreign_key="user.id", primary_key=True)
#     following_id: int  = Field(index=True, foreign_key="user.id", primary_key=True)
#     created_at: DateTime = Field(default_factory=datetime.utcnow) 
#     updated_at: DateTime = Field(default_factory=datetime.utcnow)
    
#     owner: User = Relationship(back_populates="following")
#     following: User = Relationship(back_populates="followers")
 
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

    
