import tkinter as tk


class WindowUpdateCategorie(tk.Toplevel):
    def __init__(self, master, category):
        super().__init__()
        self.title("Memo MDP - Nouvelle Catégorie")
        self.geometry('300x130')
        self.resizable(False, False)

        self.master = master
        self.category = category

        self.init_ui()

    def init_ui(self):
        frame_main = tk.Frame(self, padx=10, pady=10)
        frame_main.pack(fill='both', expand=True)

        label_title = tk.Label(frame_main, text="Update Catégorie", font=('Arial', 12, 'bold'))
        label_title.pack(fill="x")

        frame_entry = tk.Frame(frame_main, pady=10)
        frame_entry.pack(fill='x')

        label_nom = tk.Label(frame_entry, text='Nom : ')
        label_nom.grid(row=0, column=0)

        self.entry_nom = tk.Entry(frame_entry)
        self.entry_nom.insert('end', self.category.name)
        self.entry_nom.grid(row=0, column=1, sticky='we')
        frame_entry.grid_columnconfigure(1, weight=1)

        frame_button = tk.Frame(frame_main)
        frame_button.pack(fill='x')

        button_modifier = tk.Button(frame_button, text="Modifier", command=self.click_modifier, padx=10)
        button_modifier.grid(row=0, column=0)

        button_annuler = tk.Button(frame_button, text="Annuler", command=self.click_annuler, padx=10)
        button_annuler.grid(row=0, column=2, sticky='e')

        frame_button.columnconfigure(1, weight=1)
    

    def click_modifier(self):
        category = self.master.schemas.Category(
            name = self.entry_nom.get(),
            id = self.category.id
        )
        self.master.put_category(category=category)
        self.master.frame_main.frame_categorie.update_data()
        self.destroy()

    def click_annuler(self):
        self.destroy()

        






