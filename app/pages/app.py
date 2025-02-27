import tkinter as tk
from db import Base, engine, get_session
import request
import schemas


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memo MDP")

        self.test()


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


    def put_category(self) -> schemas.Category|str:
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


    def delete_category(self) -> schemas.Category|str:
        category_id = int(input("Enter category ID :"))
        with next(get_session()) as session:
            db_category = request.get_category_by_id(db=session, category_id=category_id)
            if not db_category:
                return "Category not found"
            category = request.delete_category(db=session, category=db_category)
        return schemas.Category(**category.__dict__)


    def get_motdepasse(self) -> list[schemas.Motdepasse]:
        with next(get_session()) as session:
            responses = request.get_motdepasse(db=session)
        return [self.motdepasse_models_to_schemas(response) for response in responses]


    def post_motdepasse(self) -> schemas.Motdepasse|str:
        # Fake data #####
        motdepasse = schemas.MotdepasseBase(
            name = input("Enter motdepasse name :"),
            identifiant = input("Enter motdepasse identifiant :"),
            password = input("Enter motdepasse password :"),
            description = input("Enter motdepasse description :"),
            is_tested = False,
            category = [] 
        )
        choice = 1
        while choice :
            choice = int(input("Do you want to add a category ?"))
            if choice :
                category = schemas.Category(
                    id = input("Enter category id :"),
                    name = input("Enter category name :")
                )
                motdepasse.category.append(category)
        # Fake data #####
        with next(get_session()) as session:
            if motdepasse.category:
                for cat in motdepasse.category:
                    r = request.get_category_by_id(db=session, category_id=cat.id)
                    if not r:
                        return "Category not found" 
            response = request.create_motdepasse(db=session, motdepasse=motdepasse)
        return self.motdepasse_models_to_schemas(response)


    def put_motdepasse(self) -> schemas.Motdepasse|str:
        pass


    def delete_motdepasse(self) -> schemas.Motdepasse|str:
        pass

    def motdepasse_models_to_schemas(self, motdepasse):
        categories = motdepasse.category
        categories = [schemas.Category(**category.__dict__) for category in categories]
        return schemas.Motdepasse(
            id = motdepasse.id,
            name = motdepasse.name, 
            identifiant = motdepasse.identifiant,
            password = motdepasse.password,
            description = motdepasse.description,
            is_tested = motdepasse.is_tested,
            category = categories
        )

    def test(self):

        print("\n")
        print(self.get_category())
        print("\n")
        # self.post_motdepasse()
        print("\n")
        print(self.get_motdepasse())


