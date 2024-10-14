from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.learners import Learner
from interface.date_picker import DatePicker
class RegisterPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title = ctk.CTkLabel(self, text="Register New User", font=("Arial", 24, "bold"))
        self.title.pack(pady=20)
        self.date_of_birth = ""
        self.username_entry = self.place_entry("Username:")
        self.first_name_entry = self.place_entry("First Name:")
        self.last_name_entry = self.place_entry("Last Name:")
        self.contact_num_entry = self.place_entry("Contact Number:")
        self.age_entry = self.place_entry("Age:")
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
        
    def place_entry(self, label):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack(pady=5)
        return self.entry

    def show_success_message(self):
        CTkMessagebox(title="Success", message="User registered successfully!", icon="check").pack()

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

        if not all(entry_values.values()):
            self.alert_var.set("All fields are required!")
            return

        if not self.check_age(entry_values["age"]):
            self.alert_var.set("Invalid age!")
            return
        
        if entry_values["gender"] == "Select your gender":
            self.alert_var.set("Please select a valid gender!")
            return
        if Learner.register(entry_values):
            self.show_success_message()
            self.clear_fields()
        else:
            self.alert_var.set("Failed to register user!, contact support if the issue persists.")

    def get_entry_values(self):
        return {
            "username": self.username_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "contact_num": self.contact_num_entry.get(),
            "age": self.age_entry.get(),
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

    def check_age(self, age):
        try:
            age = int(age)
            if age < 0:
                raise ValueError
        except ValueError:
            self.alert_var.set("Invalid age!")
            return False
        return True
    
    def clear_fields(self):
        for entry in [self.first_name_entry, self.last_name_entry, self.contact_num_entry, 
                      self.age_entry, self.country_entry, self.date_of_birth_entry, self.password_entry]:
            entry.delete(0, 'end')
        self.gender_combobox.set("Please select your gender")
        self.alert_var.set("") 

    def show_register_page(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_register_page(self):
        self.pack_forget()
    
    

if __name__ == "__main__":
    root = ctk.CTk()
    register_page = RegisterPage(root)
    root.geometry("800x600")
    register_page.pack(expand=True, fill="both")
    root.mainloop()

