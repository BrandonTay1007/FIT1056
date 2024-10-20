import customtkinter as ctk
from interface.tutors_assignment_to_grade_page import GradingListPage
from interface.forum_list import ForumList
from interface.profile_page import ProfilePage
from interface.edit_lessons_list_page import EditLessonsListPage
from app import *
class TutorMenu(ctk.CTkFrame):

    def __init__(self, master, user, EmpowerU):
    
        super().__init__(master=master)
        self.master = master 
        self.user = user 
        self.EmpowerU = EmpowerU
        self.user.menu = self

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome in, {user.first_name}!")
        self.welcome_label.grid(row=0, columnspan=2, padx=60, pady=10)

        self.label1 = ctk.CTkLabel(self, text="Choose one of the following:")
        self.label1.grid(row=1, columnspan=2, padx=60, pady=10)

        button_width = 200  # Set a consistent width for all buttons

        self.forum_button = ctk.CTkButton(master=self, text="Forum", width=button_width, height=40, command=self.go_to_forum_list)
        self.forum_button.grid(row=2, columnspan=2, padx=60, pady=10)

        self.grade_button = ctk.CTkButton(master=self, text="Grade Assignments", width=button_width, height=40, command=self.go_to_grade_assingment_page)
        self.grade_button.grid(row=3, columnspan=2, padx=60, pady=10)

        self.profile_button = ctk.CTkButton(master=self, text="Profile", width=button_width, height=40, command=self.go_to_profile_page)
        self.profile_button.grid(row=5, columnspan=2, padx=60, pady=10)
        
        self.logout_button = ctk.CTkButton(master=self, text="Log Out", width=button_width, height=40, command=self.logout)
        self.logout_button.grid(row=6, columnspan=2, padx=60, pady=10)


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
        self.EmpowerU.go_to_homepage()
        self.EmpowerU.user = None

    def show_page(self):
        self.place(relx=.5, rely=.5, anchor=ctk.CENTER)

    def hide_page(self):
        self.place_forget()

    def go_to_profile_page(self):
        self.hide_page()
        if not hasattr(self.user, "profile_page"):
            self.user.profile_page = ProfilePage(self.master, self.user)
        self.user.profile_page.show_page()

    def go_to_edit_lessons(self):
        self.hide_page()
        if not hasattr(self.user, "edit_lessons_page"):
            self.user.edit_lessons_page = EditLessonsListPage(self.master, self.user)
        self.user.edit_lessons_page.show_page()
