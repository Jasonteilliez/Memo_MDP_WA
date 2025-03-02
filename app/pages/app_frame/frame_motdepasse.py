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

    def update_scrollbar(self):
        self.controller.update()
        self.update_h_scroll()
        self.update_v_scroll()


    def update_v_scroll(self):
        pass
        # self.v_scroll.grid_forget()

        # if not self.tree.get_children():
        #     return

        # for child in self.tree.get_children():
        #     if not self.tree.bbox(child) or self.tree.bbox(child)[1]+self.tree.bbox(child)[3] > self.tree.winfo_height():
        #         self.v_scroll.grid(row=0, column=1, sticky="ns")
        #         return


    def update_h_scroll(self):
        pass
        # self.h_scroll.grid_forget()
        # width = 0
        # for column in self.column: 
        #     width += self.tree.column(column, "width")

        # if width > self.tree.winfo_width() :
        #     self.h_scroll.grid(row=1, column=0, sticky="ew")
       

