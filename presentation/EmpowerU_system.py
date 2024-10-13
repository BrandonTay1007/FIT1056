import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from interface.homepage import HomePage



class EmpowerU_system:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("EmpowerU")
        self.root.geometry("1200x800")
        self.homepage = HomePage(self.root)
        self.homepage.show_homepage()

if __name__ == "__main__":
    empoweru_system = EmpowerU_system()
    empoweru_system.root.mainloop()
    