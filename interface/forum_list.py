import customtkinter as ctk
from app.forum import forum

class ForumList(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.forum = forum()

    