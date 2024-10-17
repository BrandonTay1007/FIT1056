import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.user import User
from app.course import Course
from interface.lecture_selection_page_concept import LectureSelectionPage

class LearnersMenu(ctk.CTkFrame):

    def __init__(self, master, user):
        super().__init__(master=master, fg_color='transparent')  # Set width and height
        self.master = master 
        self.user = user 
        self.user.menu = self
        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome in, {user.first_name}!")
        self.welcome_label.grid(row=0, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered

        self.label1 = ctk.CTkLabel(self, text="Choose one of the following:")
        self.label1.grid(row=1, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered

        self.course_button = ctk.CTkButton(master=self, text="Course", width=100, height=40, command=self.go_to_course)
        self.course_button.grid(row=2, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered

        self.grade_button = ctk.CTkButton(master=self, text="Grade", width=100, height=40)
        self.grade_button.grid(row=3, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered

        self.profile_button = ctk.CTkButton(master=self, text="Profile", width=100, height=40)
        self.profile_button.grid(row=4, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered
        
        self.logout_button = ctk.CTkButton(master=self, text="Log Out", width=100, height=40, command=self.logout)
        self.logout_button.grid(row=5, columnspan=2, padx=60, pady=10, sticky='ew')  # Centered

        self.show_page()

    def go_to_course(self):
        self.hide_page()
        lecture_selection_page = LectureSelectionPage(self.master, self.user)
        lecture_selection_page.show_page()

    def logout(self):
        self.hide_page()
        self.master.show_homepage()

    def show_page(self):
        self.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the master

    def hide_page(self):
        self.pack_forget()
    
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Learners Menu")
    root.geometry("600x700")
    u = User(1, "JohnDoe", "password", "John", "Doe", "learner", "tseting", "testing", "testing", "testing")    
    learners_menu = LearnersMenu(root, u)
    root.mainloop()
