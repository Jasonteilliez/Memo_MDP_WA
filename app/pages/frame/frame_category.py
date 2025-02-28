import tkinter as tk
from tkinter import ttk

class FrameCategorie(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.init_ui()
        self.display_data()


    def init_ui(self):
        label_title = tk.Label(self, text="Catégorie Option", font=('Arial', 16, 'bold'))
        label_title.pack(fill="x", pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Categorie"), show="headings")
        self.tree.pack(fill="both", expand=True)

        self.tree.heading("ID", text="ID",)
        self.tree.heading("Categorie", text="Catégorie")

        self.tree.column('ID', width=80, stretch=False)

        frame_action = tk.Frame(self)
        frame_action.pack(fill="x")

        button_modifier = tk.Button(frame_action, text="Modifier Selection")
        button_modifier.grid(row=0, column=0)
        
        button_supprimer = tk.Button(frame_action, text="Supprimer Selection")
        button_supprimer.grid(row=0, column=1)

        button_Ajouter = tk.Button(frame_action, text="Ajouter Catégorie")
        button_Ajouter.grid(row=0, column=2, sticky='e')

        frame_action.columnconfigure(2, weight=1)

    def display_data(self):
        for line in self.controller.category:
            self.tree.insert("", "end", values=(line.id, line.name))
    

