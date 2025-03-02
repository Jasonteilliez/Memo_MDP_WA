import tkinter as tk
from tkinter import ttk

from .frame_category import FrameCategorie
from .frame_motdepasse import FrameMotdepasse

class FrameMain(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.init_ui(master)


    def init_ui(self, master):
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Create frames for tabs
        tab_motdepasse = ttk.Frame(notebook)
        tab_categorie = ttk.Frame(notebook)

        # Add tabs to the Notebook
        notebook.add(tab_motdepasse, text="Mot de passe")
        notebook.add(tab_categorie, text="Catégorie")

        self.frame_motdepasse = FrameMotdepasse(tab_motdepasse, master)
        self.frame_motdepasse.pack(expand=True, fill='both', padx=10, pady=10)

        self.frame_categorie = FrameCategorie(tab_categorie, master)
        self.frame_categorie.pack(expand=True, fill='both', padx=10, pady=10)

        notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event):
        self.frame_categorie.update_scrollbar()







    