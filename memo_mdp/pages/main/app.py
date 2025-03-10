import tkinter as tk
from db import Base, engine, get_session
import request
import schemas
from pages import WindowAddCategorie, WindowUpdateCategorie, WindowAddMotdepasse, WindowUpdateMotdepasse
from . import FrameMain

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memo MDP")
        self.minsize(500,400)

        self.schemas = schemas

        self.category = []
        self.motdepasse = []
        

        self.window_add_categorie = WindowAddCategorie
        self.window_update_categorie = WindowUpdateCategorie
        self.window_add_motdepasse = WindowAddMotdepasse
        self.window_update_motdepasse = WindowUpdateMotdepasse

        self.frame_main = FrameMain(self)
        self.frame_main.pack(expand=True, fill='both')

        self.update_data()


    def create_tables(self):
        Base.metadata.create_all(bind=engine)


    def get_category(self) -> list[schemas.Category]:
        with next(get_session()) as session:
            responses = request.get_category(db=session)
        return [schemas.Category(**category.__dict__) for category in responses]


    def post_category(self, category : schemas.CategoryBase) -> schemas.Category:
        with next(get_session()) as session:
            category = request.create_category(db=session, category=category)
            self.update_data()
        return schemas.Category(**category.__dict__)


    def put_category(self, category = schemas.Category) -> schemas.Category|str:
        with next(get_session()) as session:
            db_category = request.get_category_by_id(db=session, category_id=category.id)
            if not db_category:
                return "Category not found"
            category = request.update_category(db=session, category=db_category, new_category=category)
        self.update_data()
        return schemas.Category(**category.__dict__)


    def delete_category(self, category_id: int) -> str:
        with next(get_session()) as session:
            db_category = request.get_category_by_id(db=session, category_id=category_id)
            if not db_category:
                return "Category not found"
            request.delete_category(db=session, category=db_category)
        return "Category delete."


    def get_motdepasse(self) -> list[schemas.Motdepasse]:
        with next(get_session()) as session:
            responses = request.get_motdepasse(db=session)
        return [self.motdepasse_models_to_schemas(response) for response in responses]


    def post_motdepasse(self, motdepasse: schemas.MotdepasseBase) -> schemas.Motdepasse|str:
        with next(get_session()) as session:
            if motdepasse.category:
                for cat in motdepasse.category:
                    r = request.get_category_by_id(db=session, category_id=cat.id)
                    if not r:
                        return "Category not found" 
            response = request.create_motdepasse(db=session, motdepasse=motdepasse)
            self.update_data()
        return self.motdepasse_models_to_schemas(response)


    def put_motdepasse(self, motdepasse: schemas.Motdepasse) -> schemas.Motdepasse|str:
        with next(get_session()) as session:
            db_motdepasse = request.get_motdepasse_by_id(db=session, motdepasse_id=motdepasse.id)
            if not db_motdepasse:
                return "Mot de passe not found"          
            response = request.update_motdepasse(db=session, motdepasse=db_motdepasse, new_motdepasse=motdepasse)
        self.update_data()
        return self.motdepasse_models_to_schemas(response)


    def delete_motdepasse(self, motdepasse_id: int) -> str:
        with next(get_session()) as session:
            db_motdepasse = request.get_motdepasse_by_id(db=session, motdepasse_id=motdepasse_id)
            if not db_motdepasse:
                return "Mot de passe not found"
            request.delete_motdepasse(db=session, motdepasse=db_motdepasse)
        return "Mot de passe delete"


    def motdepasse_models_to_schemas(self, motdepasse) -> schemas.Motdepasse:
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


    def update_data(self):
        self.category = self.get_category()
        self.motdepasse = self.get_motdepasse()
        self.frame_main.update_display()


    def find_category_by_id(self, search_id: int) -> schemas.category: 
        for category in self.category:
            if search_id == category.id:
                return category


    def find_motdepasse_by_id(self, search_id: int) -> schemas.Motdepasse:
        for motdepasse in self.motdepasse:
            if search_id == motdepasse.id:
                return motdepasse


    def test_api(self):
        # ToDo :Need to add data
        continuer = True
        while continuer:
            print("Options disponibles :")
            print("0 : Lire categories")
            print("1 : Ajouter category")
            print("2 : Supprimer category")
            print("3 : Modifier category")
            print("4 : Lire motdepasse")
            print("5 : Ajouter motdepasse")
            print("6 : Supprimer motdepasse")
            print("7 : Mettre à jour motdepasse")
            print("8 : Create tables")
            print("9 : quitter")

            choice = input("Entrez le numéro de l'opération : ")

            if choice == "0":
                print("######################################################")
                print("### get category ###")
                list = self.get_category()
                print("\n")
                for l in list:
                    print([l])
                print("######################################################")
            elif choice == "1":
                print("######################################################")
                print("### post category ###")
                r = self.post_category()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "2":
                print("######################################################")
                print("### delete category ###")
                r = self.delete_category()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "3":
                print("######################################################")
                print("### put category ###")
                r = self.put_category()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "4":
                print("######################################################")
                print("### get motdepasse ###")
                list = self.get_motdepasse()
                print("\n")
                for l in list:
                    print([l])
                print("######################################################")
            elif choice == "5":
                print("######################################################")
                print("### post motdepasse ###")
                r = self.post_motdepasse()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "6":
                print("######################################################")
                print("### delete motdepasse ###")
                r = self.delete_motdepasse()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "7":
                print("######################################################")
                print("### put motdepasse ###")
                r = self.put_motdepasse()
                print("\n")
                print(r)
                print("######################################################")
            elif choice == "8":
                self.create_tables()
            elif choice == "9":
                continuer = False
            else:
                print("Choix invalide.")


