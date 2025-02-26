import tkinter as tk
from db import Base, engine, get_session
import request
import schemas


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memo MDP")




    def create_tables(self):
        Base.metadata.create_all(bind=engine)


    def get_category(self) -> list[schemas.Category]:
        with next(get_session()) as session:
            responses = request.get_category(db=session)
        return [schemas.Category(**category.__dict__) for category in responses]


    def post_category(self) -> schemas.Category:
        category = schemas.CategoryBase(
            name = input("Enter category name :")
        )
        with next(get_session()) as session:
            category = request.create_category(db=session, category=category)
        return schemas.Category(**category.__dict__)


    def put_category(self) -> schemas.Category:
        category = schemas.Category(
            name = input("Enter category name :"),
            id = int(input("Enter category id :"))
        )
        with next(get_session()) as session:
            db_category = request.get_category_by_id(db=session, category_id=category.id)
            if not db_category:
                return "Category not found"
            category = request.update_category(db=session, category=db_category, new_category=category)
        return schemas.Category(**category.__dict__)


    def delete_category(self) -> schemas.Category|None:
        category_id = int(input("Enter category ID :"))
        with next(get_session()) as session:
            db_category = request.get_category_by_id(db=session, category_id=category_id)
            if not db_category:
                return "Category not found"
            category = request.delete_category(db=session, category=db_category)
        return schemas.Category(**category.__dict__)


    def test(self):
        self.put_category()
