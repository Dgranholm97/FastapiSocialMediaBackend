from fastapi import APIRouter

from app.api.endpoints import like, post, user, comment, follow, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(like.router, prefix="/likes",tags=["like"])
api_router.include_router(post.router, prefix="/posts", tags=["posts"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(comment.router, prefix="/comments", tags=["comments"])
api_router.include_router(follow.router, prefix="/follows", tags=["follows"])
