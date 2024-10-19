import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.tutors import Tutor
from interface.grading_list_page import GradingListPage
from interface.forum_list import ForumList

class TutorMenu(ctk.CTkFrame):

    def __init__(self, master, user):
    
        super().__init__(master=master)
        self.master = master 
        self.user = user 
        self.user.menu = self

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome in, {user.first_name}!")
        self.welcome_label.grid(row=0, columnspan=2, padx=60, pady=10)

        self.label1 = ctk.CTkLabel(self, text="Choose one of the following:")
        self.label1.grid(row=1, columnspan=2, padx=60, pady=10)

        self.forum_button = ctk.CTkButton(master=self, text="Forum", width=100, height=40, command=self.go_to_forum_list)
        self.forum_button.grid(row=2, columnspan=2, padx=60, pady=10)

        self.grade_button = ctk.CTkButton(master=self, text="Grade Assignments", width=100, height=40, command=self.go_to_grade_assingment_page)
        self.grade_button.grid(row=3, columnspan=2, padx=60, pady=10)

        self.edit_lecture_button = ctk.CTkButton(master=self, text="Edit Lecture", width=100, height=40)
        self.edit_lecture_button.grid(row=4, columnspan=2, padx=60, pady=10)
        
        self.logout_button = ctk.CTkButton(master=self, text="Log Out", width=100, height=40, command=self.logout)
        self.logout_button.grid(row=5, columnspan=2, padx=60, pady=10)

    def go_to_forum_list(self):
        self.hide_page()
        if not hasattr(self.user, "forum_list"):
            self.user.forum_list = ForumList(self.master, self.user)
        self.user.forum_list.show_page()

    def go_to_grade_assingment_page(self):
        self.hide_page()
        if not hasattr(self.user, "grading_list_page"):
            self.user.grading_list_page = GradingListPage(self.master, self.user)
        self.user.grading_list_page.show_page()

    def logout(self):
        self.hide_page()
        self.master.show_homepage()

    def show_page(self):
        self.place(relx=.5, rely=.5, anchor=ctk.CENTER)

    def hide_page(self):
        self.place_forget()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x1200")
    tutor = Tutor.init_by_id("T0001")
    tutor_menu = TutorMenu(root, tutor)
    tutor_menu.show_page()
    root.mainloop()

