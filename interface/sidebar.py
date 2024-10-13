import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=200, height=700)
        # Add your sidebar widgets here
    
    def add_button(self, text, command):
        button = ctk.CTkButton(self, text=text, command=command)
        button.pack(pady=10, padx=10, fill="x")
        return button


def some_function():
    print("Button clicked!")

# def main():
#     root = ctk.CTk()
#     root.title("EmpowerU Login")
#     root.geometry("900x800")
#     sidebar = Sidebar(root)
#     sidebar.pack(side="left", fill="y", padx=20, pady=20)
#     sidebar.add_button("Click Me", some_function)
#     root.mainloop()


# main()