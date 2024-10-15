import customtkinter as ctk
import os

from interface.profile_page import ProfilePage
from interface.sidebar import Sidebar
from interface.grade_page import GradePage
from interface.change_password_page import ChangePassword
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
    change_password = ChangePassword(root, test_user)
    profile_page.show_page()
    sidebar.add_button("Profile", lambda: switch_page(change_password, profile_page))
    sidebar.add_button("Change Password", lambda: switch_page(profile_page, change_password))
    # grade_page = GradePage(root)
    # grade_page.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    
    # Ensure the switch_page function is correctly defined
    def switch_page(page1, page2):
        page1.hide_page()  # Ensure this method is defined in both classes
        page2.show_page()  # Ensure this method is defined in both classes

    root.mainloop()

if __name__ == "__main__":
    main()
