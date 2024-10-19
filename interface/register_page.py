from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import sys
from app.learners import Learner
from interface.date_picker import DatePicker
from app.user import User
class RegisterPage(ctk.CTkScrollableFrame):
    def __init__(self, master, empowerU_system):
        super().__init__(master)

        self.title = ctk.CTkLabel(self, text="Register New User", font=("Arial", 24, "bold"))
        self.title.pack(pady=20)
        self.empowerU_system = empowerU_system
        self.date_of_birth = ""
        self.username_entry = self.place_entry("Username:")
        self.first_name_entry = self.place_entry("First Name:")
        self.last_name_entry = self.place_entry("Last Name:")
        self.contact_num_entry = self.place_entry("Contact Number:")
        self.country_entry = self.place_entry("Country:")
        self.date_of_birth_label = ctk.CTkLabel(self, text=f"Date of Birth: {self.date_of_birth}")
        self.date_of_birth_label.pack(pady=5)
        self.date_of_birth_button = ctk.CTkButton(self, text="Select Date", command=self.place_date_picker)
        self.date_of_birth_button.pack(pady=5)
        self.gender_combobox = self.place_combobox("Gender:", ["Male", "Female"])
        self.password_entry = self.place_password_entry("Password:")

        self.alert_var = ctk.StringVar() 
        self.alert_label = ctk.CTkLabel(self, textvariable=self.alert_var, font=("Arial", 12), text_color="red")
        self.alert_label.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=20)
        
        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_main_login_page)
        self.back_button.pack()  # Place the button at the left bottom corner

        self.error_messages = []  # Add this line to store error messages

    def place_entry(self, label):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack(pady=5)
        return self.entry

    def show_success_message(self):
        CTkMessagebox(title="Success", message="User registered successfully!", icon="check")
        self.show_main_login_page()

    def place_combobox(self, label, values):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.combobox = ctk.CTkComboBox(self, values=values, width=200)
        self.combobox.set("Select your gender")
        self.combobox.configure(state="readonly")
        self.combobox.pack(pady=5)
        return self.combobox
    
    def place_password_entry(self, label):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, width=200, show="*")
        self.password_entry.pack(pady=5)
        return self.password_entry

    def register(self):
        entry_values = self.get_entry_values()

        # Check if all fields are filled
        if not all(entry_values.values()):
            CTkMessagebox(title="Error", message="All fields are required!", icon="warning")
            return

        temp_user = User(None, **entry_values)
        is_valid, self.error_messages = temp_user.register_validation(entry_values)

        if not is_valid:
            self.show_next_error()
            return

        if Learner.register(entry_values):
            self.show_success_message()
            self.clear_fields()
        else:
            CTkMessagebox(title="Error", message="Registration failed. Please try again.", icon="warning")

    def get_entry_values(self):
        return {
            "username": self.username_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "contact_num": self.contact_num_entry.get(),
            "country": self.country_entry.get(),
            "date_of_birth": self.date_of_birth,
            "gender": self.gender_combobox.get(),
            "password": self.password_entry.get()
        }

    def place_date_picker(self):
        self.date_picker = DatePicker(self)
        self.master.wait_window(self.date_picker.top)
        selected_date = self.date_picker.get_selected_date()
        if selected_date:
            self.date_of_birth = selected_date
            self.date_of_birth_label.configure(text=f"Date of Birth: {self.date_of_birth}")

    
    def clear_fields(self):
        for entry in [self.username_entry, self.first_name_entry, self.last_name_entry, 
                      self.contact_num_entry, self.country_entry, self.password_entry]:
            entry.delete(0, 'end')
        self.gender_combobox.set("Select your gender")
        self.date_of_birth = ""
        self.date_of_birth_label.configure(text="Date of Birth: ")
        self.alert_var.set("")

    def show_register_page(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_register_page(self):
        self.pack_forget()
    
    def show_main_login_page(self):
        self.hide_register_page()
        self.empowerU_system.go_to_homepage()

    def show_next_error(self):
        if self.error_messages:
            error_message = self.error_messages.pop(0)
            CTkMessagebox(title="Error", message=error_message, icon="warning")
        else:
            CTkMessagebox(title="Error", message="Unknown error occurred.", icon="warning")

        

