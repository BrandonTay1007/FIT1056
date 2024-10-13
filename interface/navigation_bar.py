import customtkinter as ctk
from sidebar import Sidebar
class NavigationBar(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(height=500, width="100%")  # Set a fixed height and width to the whole window for the navigation bar
        self.home_button = self.add_button("Home", some_function)
        self.button1 = self.add_button("Button 1", some_function)
        self.button2 = self.add_button("Button 2", some_function)
        self.button3 = self.add_button("Button 3", some_function)
        
    def add_button(self, text, command):
        button = ctk.CTkButton(self, text=text, command=command,
                               fg_color="transparent", hover_color="#4A4A4A",
                               corner_radius=0)
        button.pack(side="left", padx=5, fill="y")
        return button

def some_function():
    print("Button clicked!")

def main():
    root = ctk.CTk()
    root.title("Profile-page")
    root.geometry("900x800")
    nav_bar = NavigationBar(root)
    nav_bar.pack(side="top", fill="x", padx=20, pady=20)
    sidebar = Sidebar(root)
    sidebar.pack(side="left", fill="y", padx=20, pady=20)
    root.after(1000, lambda: root.title("Profile-page Updated"))  # Change title after 5 seconds
    root.mainloop()

main()