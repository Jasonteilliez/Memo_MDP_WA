import tkinter as tk
from tkinter import ttk, messagebox


class FrameCategorie(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.column = ("ID", "Categorie")
        self.init_ui()
        self.display_data()

        self.new_window_add = None
        self.new_window_modify = None
        

    def init_ui(self):
        label_title = tk.Label(self, text="Catégorie Option", font=('Arial', 16, 'bold'))
        label_title.pack(fill="x", pady=10)

        ### Treeview ###
        self.frame_tree = tk.Frame(self)
        self.frame_tree.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame_tree, columns=self.column, show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Categorie", text="Catégorie")

        self.tree.column("ID", width=0, stretch=False)

        self.tree["displaycolumns"] = ("Categorie")

        self.h_scroll = ttk.Scrollbar(self.frame_tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.h_scroll.set)

        self.v_scroll = ttk.Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scroll.grid(row=0, column=1, sticky="ns")
        self.h_scroll.grid(row=1, column=0, sticky="ew")

        self.frame_tree.grid_rowconfigure(0, weight=1)
        self.frame_tree.grid_columnconfigure(0, weight=1)
        ### Treeview ###

        frame_action = tk.Frame(self)
        frame_action.pack(fill="x")

        button_modifier = tk.Button(frame_action, text="Modifier Selection", command=self.open_modifier)
        button_modifier.grid(row=0, column=0)
        
        button_supprimer = tk.Button(frame_action, text="Supprimer Selection", command=self.click_supprimer)
        button_supprimer.grid(row=0, column=1)

        button_ajouter = tk.Button(frame_action, text="Ajouter Catégorie", command=self.open_ajouter)
        button_ajouter.grid(row=0, column=2, sticky='e')

        frame_action.columnconfigure(2, weight=1)


    def display_data(self):
        for line in self.controller.category:
            self.tree.insert("", "end", values=(line.id, line.name))
        self.update_scrollbar()


    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())

    
    def update_scrollbar(self):
        self.controller.update()
        self.update_h_scroll()
        self.update_v_scroll()


    def update_v_scroll(self):
        
        self.v_scroll.grid_forget()

        if not self.tree.get_children():
            return

        for child in self.tree.get_children():
            if not self.tree.bbox(child) or self.tree.bbox(child)[1]+self.tree.bbox(child)[3] > self.tree.winfo_height():
                self.v_scroll.grid(row=0, column=1, sticky="ns")
                return


    def update_h_scroll(self):
        self.h_scroll.grid_forget()
        width = 0
        for column in self.column: 
            width += self.tree.column(column, "width")

        if width > self.tree.winfo_width() :
            self.h_scroll.grid(row=1, column=0, sticky="ew")


    def update_tree(self):
        self.clear_tree()
        self.display_data()


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
        self.controller.update_data()

    def open_ajouter(self):
        if self.new_window_add is None or not self.new_window_add.winfo_exists():
            self.new_window_add = self.controller.window_add_categorie(self.controller)
            self.new_window_add.protocol("WM_DELETE_WINDOW", self.on_close_ajouter)
        
    
    def on_close_ajouter(self):
        self.new_window_add.destroy()
        self.new_window_add = None


    def open_modifier(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Warring", "No item selected. Please select an item.")
            return
        if len(selected_items)>1:
            messagebox.showwarning("Warring", "Two or more selected item. You can only modify one time at a time.")
            return
        if self.new_window_modify is None or not self.new_window_modify.winfo_exists():
            search_id = int(self.tree.item(selected_items, "values")[0])
            category = self.controller.find_category_by_id(search_id=search_id)
            self.new_window_modify = self.controller.window_update_categorie(self.controller, category)
            self.new_window_modify.protocol("WM_DELETE_WINDOW", self.on_close_modifier)
        return
    

    def on_close_modifier(self):
        self.new_window_modify.destroy()
        self.new_window_modify = None
