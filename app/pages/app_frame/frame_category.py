import tkinter as tk
from tkinter import ttk, messagebox



class FrameCategorie(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.init_ui()
        self.display_data()

        self.new_window_add = None
        self.new_window_modify = None
        

    def init_ui(self):
        label_title = tk.Label(self, text="Catégorie Option", font=('Arial', 16, 'bold'))
        label_title.pack(fill="x", pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Categorie"), show="headings")
        self.tree.pack(fill="both", expand=True)

        self.tree.heading("ID", text="ID",)
        self.tree.heading("Categorie", text="Catégorie")

        self.tree["displaycolumns"] = ("Categorie")

        frame_action = tk.Frame(self)
        frame_action.pack(fill="x")

        button_modifier = tk.Button(frame_action, text="Modifier Selection", command=self.click_modifier)
        button_modifier.grid(row=0, column=0)
        
        button_supprimer = tk.Button(frame_action, text="Supprimer Selection", command=self.click_supprimer)
        button_supprimer.grid(row=0, column=1)

        button_ajouter = tk.Button(frame_action, text="Ajouter Catégorie", command=self.open_ajouter)
        button_ajouter.grid(row=0, column=2, sticky='e')

        frame_action.columnconfigure(2, weight=1)

    def display_data(self):
        for line in self.controller.category:
            self.tree.insert("", "end", values=(line.id, line.name))

    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())


    def update_data(self):
        self.clear_tree()
        self.display_data()

    
    def click_modifier(self):
        print('modifier')


    def click_supprimer(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Warring", "No item selected. Please select an item.")
            return
        response = messagebox.askokcancel("Confirmation suppression", "Are you sure ? ")
        if response :   
            for item in selected_items:
                category_id = self.tree.item(item, "values")[0]
                self.controller.delete_category(category_id=category_id)
        self.update_data()                             


    def open_ajouter(self):
        if self.new_window_add is None or not self.new_window_add.winfo_exists():
            self.new_window_add = self.controller.window_add_categorie(self.controller)
            self.new_window_add.protocol("WM_DELETE_WINDOW", self.on_close_ajouter)
        
    
    def on_close_ajouter(self):
        self.new_window_add.destroy()
        self.new_window_add = None

    

