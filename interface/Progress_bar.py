import customtkinter as ctk

class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, master, width=300):
        super().__init__(master, width=width)
        self.set(0)

    def update_progress(self, progress):
        self.set(progress)
