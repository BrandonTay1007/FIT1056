import customtkinter as ctk
from PIL import Image
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from empoweru_constants import *
from app.learners import Learner
from app.tutors import Tutor
from app.admin import Admin
from interface.learners_menu import *
from interface.menu_tutors import *
from interface.menu_admin import *

class LoginPage(ctk.CTkFrame):

    def __init__(self, master, empowerU_system):
        super().__init__(master=master)
        self.master = master 
        self.image_path = LOGO_PATH
        self.empowerU_system = empowerU_system

        # Set the appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Load and display the image
        self.logo_image = ctk.CTkImage(Image.open(LOGO_PATH), size=(300, 300))
        self.logo_label = ctk.CTkLabel(master=self, image=self.logo_image, text="")
        self.logo_label.grid(row=0, columnspan=2, padx=10, pady=10)
            
        # Welcome heading
        self.login_title = ctk.CTkLabel(master=self, 
            text="Welcome to EmpowerU", 
            font=("Arial Bold", 30))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Dropdown (Combobox) for user type selection
        self.user_type = ctk.CTkOptionMenu(master=self, 
                                           values=["Learner", "Teacher", "Admin"],
                                           width=200,
                                           height=40)
        self.user_type.set("Select User Type")
        self.user_type.grid(row=2, columnspan=2, padx=60, pady=10)

        # Username entry widget
        self.username_entry = ctk.CTkEntry(master=self, placeholder_text="Username", width=200, height=40)
        self.username_entry.grid(row=3, columnspan=2, padx=60, pady=10)

        # Password entry widget
        self.password_entry = ctk.CTkEntry(master=self, placeholder_text="Password", show="●", width=200, height=40)
        self.password_entry.grid(row=4, columnspan=2, padx=60, pady=10)

        # Alert label widget - displays alert messages where necessary
        self.alert_label = ctk.CTkLabel(master=self, text="")
        self.alert_label.grid(row=5, columnspan=2, padx=60, pady=10)

        # Button to login
        self.login_button = ctk.CTkButton(master=self, text="Login", width=100, height=40, command=self.login_pressed)
        self.login_button.grid(row=6, columnspan=2, padx=60, pady=10)

        # Button to go back to main login page
        self.back_button = ctk.CTkButton(self, text="Back", width=100, height=40, command=self.show_main_login_page)
        self.back_button.grid(row=7, columnspan=2, padx=60, pady=10)

        # Button to shut down
        self.shutdown_button = ctk.CTkButton(master=self, text="Shut down", command=master.destroy, width=100, height=40)
        self.shutdown_button.grid(row=8, columnspan=2, padx=60, pady=10)

        # Configure grid to expand properly
        self.grid_columnconfigure((0, 1), weight=1)

    def show_login_page(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_login_page(self):
        self.pack_forget()

    def switch_page(self, empowerU_system, cur_page):
        empowerU_system.hide_page()
        cur_page.show_page()

    def login_pressed(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()

        if user_type == "Learner":
            if Learner.authenticate(username, password, LEARNERS_FILE_PATH):
                self.empowerU_system.user = Learner.init_by_username(username)
                LearnersMenu(self.empowerU_system.root, self.empowerU_system.user)
                self.hide_login_page()
                self.empowerU_system.go_to_menu()
            else:
                self.alert_label.configure(text="Invalid username or password")

        if user_type == "Teacher":
            if Tutor.authenticate(username, password, TEACHERS_FILE_PATH):
                self.empowerU_system.user = Tutor.init_by_username(username)
                TutorMenu(self.empowerU_system.root, self.empowerU_system.user)
                self.hide_login_page()
                self.empowerU_system.go_to_menu()
            else:
                self.alert_label.configure(text="Invalid username or password")

        if user_type == "Admin":
            if Admin.authenticate(username, password, ADMIN_FILE_PATH):
                self.empowerU_system.user = Admin.init_by_username(username)
                AdminMenu(self.empowerU_system.root, self.empowerU_system.user, self.empowerU_system)
                self.hide_login_page()
                self.empowerU_system.go_to_menu()
            else:
                self.alert_label.configure(text="Invalid username or password")

    def show_main_login_page(self):
        self.hide_login_page()
        self.empowerU_system.go_to_homepage()


        
