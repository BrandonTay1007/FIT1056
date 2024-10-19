import customtkinter as ctk
from PIL import Image
import os
import sys
from interface.register_page import RegisterPage
from interface.login_page import LoginPage
from app.empoweru_constants import *
class HomePage(ctk.CTkFrame):

    def __init__(self, master, empowerU_system):
        super().__init__(master=master)
        self.master = master 
        self.image_path = LOGO_PATH
        self.empowerU_system = empowerU_system
        # Set the appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
                
        # Logo image
        self.logo_image = ctk.CTkImage(Image.open(self.image_path), size=(300, 300))
        self.logo_label = ctk.CTkLabel(master=self, image=self.logo_image, text="")
        self.logo_label.grid(row=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Welcome heading
        self.login_title = ctk.CTkLabel(master=self, 
            text="Welcome to EmpowerU", 
            font=("Arial Bold", 30))
        self.login_title.grid(row=1, columnspan=2, sticky="nsew", padx=10, pady=(10, 50))  # Increased bottom padding

        # New User button
        self.new_user_button = ctk.CTkButton(master=self, text="New User", width=100, height=40, command=self.navigate_to_register_page)
        self.new_user_button.grid(row=2, columnspan=2, padx=60, pady=(0, 40))  # Increased bottom padding

        # Existing User button
        self.existing_user_button = ctk.CTkButton(master=self, text="Existing User", width=100, height=40, command=self.navigate_to_login_page)
        self.existing_user_button.grid(row=3, columnspan=2, padx=60, pady=(0, 40))  # Increased bottom padding

        # Shut Down button
        self.shut_down_button = ctk.CTkButton(master=self, text="Shut Down", width=100, height=40, command=self.shut_down)
        self.shut_down_button.grid(row=4, columnspan=2, padx=60, pady=(0, 40))  # Increased bottom padding

        # Configure grid to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_homepage(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_homepage(self):
        self.pack_forget()

    def switch_page(self, empowerU_system, cur_page):
        empowerU_system.hide_page()
        cur_page.show_page()

    def navigate_to_register_page(self):
        self.hide_homepage()
        self.current_page = RegisterPage(self.master, self.empowerU_system)
        self.current_page.show_register_page()

    def navigate_to_login_page(self):
        self.hide_homepage()
        self.current_page = LoginPage(self.master, self.empowerU_system)
        self.current_page.show_login_page()

    def shut_down(self):
        self.master.quit()


def main():
    root = ctk.CTk()
    root.title("EmpowerU Login")
    root.geometry("900x800")
    homepage = HomePage(root, "Picture/EmpowerU Logo.png")
    homepage.pack(expand=True, fill="both", padx=20, pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
