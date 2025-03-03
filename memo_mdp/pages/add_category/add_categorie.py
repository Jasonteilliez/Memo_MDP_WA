import tkinter as tk


class WindowAddCategorie(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.title("Memo MDP - Nouvelle Catégorie")
        self.geometry('300x130')
        self.resizable(False, False)

        self.master = master

        self.init_ui()

    def init_ui(self):
        frame_main = tk.Frame(self, padx=10, pady=10)
        frame_main.pack(fill='both', expand=True)

        label_title = tk.Label(frame_main, text="Nouvelle Catégorie", font=('Arial', 12, 'bold'))
        label_title.pack(fill="x")

        frame_entry = tk.Frame(frame_main, pady=10)
        frame_entry.pack(fill='x')

        label_nom = tk.Label(frame_entry, text='Nom : ')
        label_nom.grid(row=0, column=0)

        self.entry_nom = tk.Entry(frame_entry)
        self.entry_nom.grid(row=0, column=1, sticky='we')
        frame_entry.grid_columnconfigure(1, weight=1)

        frame_button = tk.Frame(frame_main)
        frame_button.pack(fill='x')

        button_ajouter = tk.Button(frame_button, text="Ajouter", command=self.click_ajouter, padx=10)
        button_ajouter.grid(row=0, column=0)

        button_annuler = tk.Button(frame_button, text="Annuler", command=self.click_annuler, padx=10)
        button_annuler.grid(row=0, column=2, sticky='e')

        frame_button.columnconfigure(1, weight=1)
    

    def click_ajouter(self):
        category = self.master.schemas.CategoryBase(
            name = self.entry_nom.get()
        )
        self.master.post_category(category=category)
        self.entry_nom.delete(0, "end")

    def click_annuler(self):
        self.destroy()

        






