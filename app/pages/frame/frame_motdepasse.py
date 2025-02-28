import tkinter as tk


class FrameMotdepasse(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.init_ui()

    def init_ui(self):
        tk.Label(self, text="mot de passe").pack()