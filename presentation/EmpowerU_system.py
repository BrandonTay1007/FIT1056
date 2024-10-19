import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from interface.register_page import RegisterPage
from interface.login_page import LoginPage
from interface.main_login_page import HomePage

class EmpowerU_system:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("EmpowerU")
        self.root.geometry("1200x800")
        
        self.main_login_page = HomePage(self.root, self)
        self.register_page = RegisterPage(self.root, self)
        self.login_page = LoginPage(self.root, self)
        
        self.current_page = self.main_login_page
        self.current_page.show_homepage()
    
    def switch_page(self, new_page):
        self._hide_current_page()
        self.current_page = new_page
        self._show_current_page()

    def go_to_registration(self):
        self.switch_page(self.register_page)

    def go_to_homepage(self):
        self.switch_page(self.main_login_page)

    def go_to_login(self):
        self.switch_page(self.login_page)

    def _hide_current_page(self):
        hide_method = getattr(self.current_page, 'hide_page', None) or getattr(self.current_page, 'hide_homepage', None)
        if hide_method:
            hide_method()

    def _show_current_page(self):
        show_method = getattr(self.current_page, 'show_page', None) or getattr(self.current_page, 'show_homepage', None)
        if show_method:
            show_method()

    def go_to_menu(self):
        self._hide_current_page()
        self.current_page = self.user.menu
        self.user.menu.show_page()

