from app.crud.base import CRUDBase
from app.models.user import Users
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    
    def __init__(self, model):
        super().__init__(model)
        
    def get_user_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()

user = CRUDUser(Users)