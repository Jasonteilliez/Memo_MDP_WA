from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Motdepasse(Base):
    __tablename__ = "motdepasse"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    identifiant = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    description = Column(String(500))
    is_tested = Column(Boolean, default=False)
    category = relationship("Category", secondary="motdepasse_category")
    