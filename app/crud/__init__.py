from .crud_comment import comment
from .crud_user import user
from .crud_post import post
from .crud_like import like
from .crud_follow import follow


# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
