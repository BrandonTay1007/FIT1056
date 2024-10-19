import customtkinter as ctk
from PIL import Image
from interface.register_page import RegisterPage

class HomePage(ctk.CTkFrame):
    register_page = None
    def __init__(self, master, empoweru_system):
        super().__init__(master=master)
        self.master = master 
        self.empoweru_system = empoweru_system
        # Set the appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
                
        # Logo image
        self.logo_image = ctk.CTkImage(Image.open("Picture/EmpowerU Logo.png"), size=(200, 205))
        self.logo_label = ctk.CTkLabel(master=self, image=self.logo_image, text="")
        self.logo_label.grid(row=0, columnspan=2, sticky="S", padx=10, pady=10)

        # Welcome heading
        self.login_title = ctk.CTkLabel(master=self, 
            text="Welcome to EmpowerU", 
            font=("Arial Bold", 30))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Dropdown (Combobox) for user type selection
        self.user_type = ctk.CTkOptionMenu(master=self, 
                                           values=["Student", "Tutor", "Admin"],
                                           width=200,
                                           height=40)
        self.user_type.set("Select User Type")  # Set default text
        self.user_type.grid(row=2, columnspan=2, padx=60, pady=10)

        # Username entry widget
        self.username_entry = ctk.CTkEntry(master=self, placeholder_text="Username", width=200, height=40)
        self.username_entry.grid(row=3, columnspan=2, padx=60, pady=10)

        # Password entry widget
        self.password_entry = ctk.CTkEntry(master=self, placeholder_text="Password", show="*", width=200, height=40)
        self.password_entry.grid(row=4, columnspan=2, padx=60, pady=10)

        # Alert label widget - displays alert messages where necessary
        self.alert_label = ctk.CTkLabel(master=self, text="")
        self.alert_label.grid(row=5, columnspan=2, padx=60, pady=10)

        # Button to login
        self.login_button = ctk.CTkButton(master=self, text="Login", width=100, height=40)
        self.login_button.grid(row=6, columnspan=2, padx=60, pady=10)

        # Button to register
        self.register_button = ctk.CTkButton(master=self, text="Register", width=100, height=40, command=empoweru_system.go_to_registration)
        self.register_button.grid(row=7, columnspan=2, padx=60, pady=10)

        # Button to shut down
        self.shutdown_button = ctk.CTkButton(master=self, text="Shut down", command=master.destroy, width=100, height=40)
        self.shutdown_button.grid(row=8, columnspan=2, padx=60, pady=10)

        # Configure grid to expand properly
        self.grid_columnconfigure((0, 1), weight=1)

    def show_page(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_page(self):
        self.pack_forget()
    
    def login(self):
        # username = self.username_entry.get()
        # password = self.password_entry.get()
        # if self.user_type.get() == 'Student':
        #     user = app.Student.authenticate(username, password)
        # elif self.user_type.get() == 'Tutor':
        #     user = app.Tutor.authenticate(username, password)
        # elif self.user_type.get() == 'Admin':
        #     user = app.Admin(username, password)
        # WE GOT USER OBEJCT
        pass    
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x800")
    homepage = HomePage(root, None)
    homepage.show_page()
    root.mainloop()

