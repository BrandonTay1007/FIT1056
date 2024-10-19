import customtkinter as ctk
import sys
import os
# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface.admin_add_user_page import AdminAddUserPage
from interface.admin_edit_user_page import AdminEditUserPage

class AdminMenu(ctk.CTkFrame):

    def __init__(self, master, admin, EmpowerU):
        super().__init__(master=master, fg_color="transparent")
        self.master = master 
        self.admin = admin 
        self.EmpowerU = EmpowerU
        self.admin.menu = self
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome in, {admin.first_name}!")
        self.welcome_label.grid(row=0, columnspan=2, padx=60, pady=10)

        self.label1 = ctk.CTkLabel(self, text="Choose one of the following:")
        self.label1.grid(row=1, columnspan=2, padx=60, pady=10)

        self.add_new_user_button = ctk.CTkButton(master=self, text="Add New User", width=100, height=40, command=self.go_to_add_new_user_page)
        self.add_new_user_button.grid(row=2, columnspan=2, padx=60, pady=10)

        self.edit_user_button = ctk.CTkButton(master=self, text="Edit User", width=100, height=40, command=self.go_to_edit_user_page)
        self.edit_user_button.grid(row=3, columnspan=2, padx=60, pady=10)
        
        self.logout_button = ctk.CTkButton(master=self, text="Log Out", width=100, height=40, command=self.logout)
        self.logout_button.grid(row=4, columnspan=2, padx=60, pady=10)
    
    def go_to_page(self, page_type, attribute_name):
        self.hide_page()
        if not hasattr(self.admin, attribute_name):
            setattr(self.admin, attribute_name, page_type(self.master, self.admin))
        getattr(self.admin, attribute_name).show_page()

    def go_to_edit_user_page(self):
        self.go_to_page(AdminEditUserPage, 'edit_user_page')

    def go_to_add_new_user_page(self):
        self.go_to_page(AdminAddUserPage, 'add_user_page')

    def logout(self):
        self.hide_page()
        self.EmpowerU.go_to_homepage()
        self.EmpowerU.user = None

    def show_page(self):
        self.place(relx=0.5, rely=0.5, anchor="center")

    def hide_page(self):
        self.place_forget()
