import tkinter as tk


class WindowUpdateMotdepasse(tk.Toplevel):
    def __init__(self, master, motdepasse):
        super().__init__()
        self.title("Memo MDP - Update Mot de passe")
        self.master = master
        self.motdepasse = motdepasse

        self.list_val = {}

        self.init_ui()

    def init_ui(self):
        frame_main = tk.Frame(self, padx=10, pady=10)
        frame_main.pack(fill='both', expand=True)

        label_title = tk.Label(frame_main, text="Nouveau Mot de passe", font=('Arial', 12, 'bold'))
        label_title.pack(fill="x")

        frame_entry = tk.Frame(frame_main, pady=10)
        frame_entry.pack(fill='x')

        self.is_tested = tk.BooleanVar()
        cb_is_tested = tk.Checkbutton(frame_entry, text='Verify ?', variable=self.is_tested)
        label_nom = tk.Label(frame_entry, text='Nom : ')
        label_identifiant = tk.Label(frame_entry, text='Identifiant : ')
        label_password = tk.Label(frame_entry, text='Mot de passe : ')
        label_description = tk.Label(frame_entry, text='Description : ')
        cb_is_tested.grid(row=0, column=0, sticky='w')
        label_nom.grid(row=1, column=0, sticky='w')
        label_identifiant.grid(row=2, column=0, sticky='w')
        label_password.grid(row=3, column=0, sticky='w')
        label_description.grid(row=4, column=0, sticky='w')

        self.entry_name = tk.Entry(frame_entry)
        self.entry_identifiant = tk.Entry(frame_entry)
        self.entry_password = tk.Entry(frame_entry)
        self.entry_description = tk.Entry(frame_entry)
        self.entry_name.grid(row=1, column=1, sticky='we')
        self.entry_identifiant.grid(row=2, column=1, sticky='we')
        self.entry_password.grid(row=3, column=1, sticky='we')
        self.entry_description.grid(row=4, column=1, sticky='we')
        frame_entry.grid_columnconfigure(1, weight=1)

        self.is_tested.set(self.motdepasse.is_tested)
        self.entry_name.insert('end', self.motdepasse.name)
        self.entry_identifiant.insert('end', self.motdepasse.identifiant)
        self.entry_password.insert('end', self.motdepasse.password)
        self.entry_description.insert('end', self.motdepasse.description)

        frame_category = tk.Frame(frame_main)
        frame_category.pack(fill='x')

        for index, category in enumerate(self.master.category):
            var = tk.BooleanVar()
            for cat in self.motdepasse.category:
                if cat.id == category.id:
                    var.set(True)
            cb = tk.Checkbutton(frame_category, text=category.name, variable=var)
            row = index//4
            column = index%4
            frame_category.grid_columnconfigure(column, minsize=100)
            cb.grid(row=row,column=column, sticky='w')
            self.list_val[category.id] = var

        frame_button = tk.Frame(frame_main)
        frame_button.pack(fill='x')

        button_ajouter = tk.Button(frame_button, text="Modifier", command=self.click_modifier, padx=10)
        button_ajouter.grid(row=0, column=0)

        button_annuler = tk.Button(frame_button, text="Annuler", command=self.click_annuler, padx=10)
        button_annuler.grid(row=0, column=2, sticky='e')

        frame_button.columnconfigure(1, weight=1)
    

    def click_modifier(self):
        motdepasse = self.master.schemas.Motdepasse(
            id = self.motdepasse.id,
            name = self.entry_name.get(),
            identifiant = self.entry_identifiant.get(),
            password = self.entry_password.get(),
            description = self.entry_description.get(),
            is_tested = self.is_tested.get(),
            category = [] 
        )
        for id, val in self.list_val.items():
            if val.get():
                category = self.master.find_category_by_id(search_id=id)
                if category:
                    motdepasse.category.append(category)
        self.master.put_motdepasse(motdepasse=motdepasse)
        self.destroy()

    def click_annuler(self):
        self.destroy()


