import tkinter as tk
from tkinter import ttk

from .frame_category import FrameCategorie
from .frame_motdepasse import FrameMotdepasse

class FrameMain(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.init_ui(master)


    def init_ui(self, master):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.tab_motdepasse = ttk.Frame(self.notebook)
        self.tab_categorie = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_motdepasse, text="Mot de passe")
        self.notebook.add(self.tab_categorie, text="Catégorie")

        self.frame_motdepasse = FrameMotdepasse(self.tab_motdepasse, master)
        self.frame_motdepasse.pack(expand=True, fill='both', padx=10, pady=10)

        self.frame_categorie = FrameCategorie(self.tab_categorie, master)
        self.frame_categorie.pack(expand=True, fill='both', padx=10, pady=10)

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event):
        selected_tab = self.notebook.select()
        if selected_tab == ".!framemain.!notebook.!frame":
            self.frame_motdepasse.update_scrollbar()
        elif selected_tab == ".!framemain.!notebook.!frame2":
            self.frame_categorie.update_scrollbar()
        return







    