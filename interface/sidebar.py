import customtkinter as ctk

class Sidebar(ctk.CTkScrollableFrame):
    def __init__(self, master, width=200, height=700):
        super().__init__(master)
        self.configure(width=width, height=height)

        # Add your sidebar widgets here
    
    def add_button(self, text, command, color="transparent", align="center"):
        # Create button with specified alignment
        button = ctk.CTkButton(self, text=text, width=self.winfo_width(), fg_color=color, anchor=align, command=command)
        button.pack(pady=10, padx=10, fill="x")
        return button

    def show_sidebar(self):
        self.pack(side="left", fill="y", padx=20, pady=20)

    def hide_sidebar(self):
        self.pack_forget()

# def main():
#     root = ctk.CTk()
#     root.title("EmpowerU Login")
#     root.geometry("900x800")
#     sidebar = Sidebar(root)
#     sidebar.pack(side="left", fill="y", padx=20, pady=20)
#     sidebar.add_button("Click Me", some_function)
#     root.mainloop()


# main()
