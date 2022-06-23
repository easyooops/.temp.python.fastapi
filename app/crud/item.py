from app.crud.base import CRUDBase
from app.models.item import Items
from app.schemas.item import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session

class CRUDItem(CRUDBase[Items, ItemCreate, ItemUpdate]):
    
    def __init__(self, model):
        super().__init__(model)
        
    def create_user_item(self, db: Session, item: ItemCreate, user_id: int):
        db_item = Items(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

item = CRUDItem(Items)