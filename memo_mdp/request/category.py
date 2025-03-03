from sqlalchemy.orm import Session
import schemas
from models import Category


def create_category(db: Session, category: schemas.CategoryBase):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_id(db: Session, category_id: int):
    db_category = db.get(Category, category_id)
    return db_category


def get_category(db: Session):
    return db.query(Category).all()


def delete_category(db: Session, category: schemas.Category):
    db.delete(category)
    db.commit()
    return category


def update_category(db: Session, category: schemas.Category, new_category: schemas.Category):
    category.name = new_category.name
    db.commit()
    db.refresh(category)
    return category
