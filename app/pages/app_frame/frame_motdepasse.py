import tkinter as tk


class FrameMotdepasse(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.init_ui()
        

    def init_ui(self):
        label_title = tk.Label(self, text="Mot De Passe", font=('Arial', 16, 'bold'))
        label_title.pack(fill="x", pady=10)

        frame_search = tk.Frame(self).pack(fill="x", pady=10)
        frame_category = tk.Frame(self).pack(fill="x", pady=10)
        frame_motdepasse = tk.Frame(self).pack(fill="x", expand=True, pady=10)

        

