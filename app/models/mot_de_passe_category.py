from sqlalchemy import Column, ForeignKey, Integer
from db import Base


class MotdepasseCategory(Base):
    __tablename__ = "motdepasse_category"

    id = Column(Integer, primary_key=True)
    motdepasse_id = Column('motdepasse_id', Integer, ForeignKey('motdepasse.id', ondelete='CASCADE'))
    category_id = Column('category_id', Integer, ForeignKey('category.id', ondelete='CASCADE'))                        
