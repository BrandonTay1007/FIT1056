import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from interface.register_page import RegisterPage
from interface.homepage import HomePage
# from interface.login_page import LoginPage

class EmpowerU_system:
    user = None
    registration_page = None
    homepage = None
 
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("EmpowerU")
        self.root.geometry("1200x800")
        
        self.homepage = HomePage(self.root, self)
        self.registration_page = RegisterPage(self.root, self)  # Pass the instance for navigation
        self.homepage.show_page()
        self.registration_page.hide_page()
        
    def switch_page(self, cur_page, new_page):
        cur_page.hide_page()
        new_page.show_page()

    def go_to_registration(self):
        self.switch_page(self.homepage, self.registration_page)

    def go_to_homepage(self):
        self.switch_page(self.registration_page, self.homepage)

if __name__ == "__main__":
    empoweru_system = EmpowerU_system()
    empoweru_system.root.mainloop()
    
