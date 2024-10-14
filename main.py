import customtkinter as ctk
import os

from interface.profile_page import ProfilePage
from interface.sidebar import Sidebar
from interface.grade_page import GradePage
from app.user import User
from interface.homepage import HomePage
from interface.register_page import RegisterPage


def main():
    test_user = User("L0001", "JohnDoe", "password", "John", "Doe", "0123456789", 20, "Malaysia", "01/01/2000", "Male")
    root = ctk.CTk()
    root.title("Settings")
    root.geometry("1200x800")
    
        
    sidebar = Sidebar(root)
    sidebar.show_sidebar()
    
    # Create and pack the profile page
    profile_page = ProfilePage(root, test_user)
    profile_page.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    
    # grade_page = GradePage(root)
    # grade_page.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    
    root.mainloop()
if __name__ == "__main__":
    main()