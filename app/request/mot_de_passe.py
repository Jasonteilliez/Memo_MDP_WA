from sqlalchemy.orm import Session
import schemas
from models import Motdepasse
from .category import get_category_by_id


def create_motdepasse(db: Session, motdepasse: schemas.MotdepasseBase):
    category = [get_category_by_id(db=db, category_id=cat.id) for cat in motdepasse.category]
    print(category)
    db_motdepasse = Motdepasse(
        name=motdepasse.name,
        identifiant=motdepasse.identifiant,
        password=motdepasse.password,
        description=motdepasse.description,
        is_tested=False,
        category= category
    )
    db.add(db_motdepasse)
    db.commit()
    db.refresh(db_motdepasse)
    return db_motdepasse


def get_motdepasse_by_id(db: Session, motdepasse_id: int):
    db_motdepasse = db.get(Motdepasse, motdepasse_id)
    return db_motdepasse


def get_motdepasse(db: Session):
    return db.query(Motdepasse).all()


def delete_motdepasse(db: Session, motdepasse: schemas.Motdepasse):
    db.delete(motdepasse)
    db.commit()
    return motdepasse


def update_motdepasse(db: Session, motdepasse: schemas.Motdepasse, new_motdepasse: schemas.Motdepasse):
    category = [get_category_by_id(db=db, category_id=cat.id) for cat in new_motdepasse.category]
    motdepasse.name=new_motdepasse.name
    motdepasse.identifiant=new_motdepasse.identifiant
    motdepasse.password=new_motdepasse.password
    motdepasse.description=new_motdepasse.description
    motdepasse.is_tested=new_motdepasse.is_tested
    motdepasse.category= category
    db.commit()
    db.refresh(motdepasse)
    return motdepasse
