from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import sys
import os
import uuid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.admin import Admin
from app.learners import Learner
import empoweru_constants as constants
from interface.date_picker import DatePicker

class AdminAddUserPage(ctk.CTkScrollableFrame):
    def __init__(self, master, empoweru_system):
        super().__init__(master)

        self.title = ctk.CTkLabel(self, text="Add New User", font=("Arial", 24, "bold"))
        self.title.pack(pady=20)

        self.user_type_combobox = self.place_combobox("User Type:", ["Student", "Admin"])
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
        self.profile_picture_entry = self.place_entry("Profile Picture Path:")


        self.alert_var = ctk.StringVar() 
        self.alert_label = ctk.CTkLabel(self, textvariable=self.alert_var, font=("Arial", 12), text_color="red")
        self.alert_label.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Add User", command=self.add_user)
        self.add_button.pack(pady=20)
        
        self.back_button = ctk.CTkButton(self, text="Back", command=None)
        self.back_button.pack()

    def place_entry(self, label):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack(pady=5)
        return self.entry

    def place_combobox(self, label, values):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.combobox = ctk.CTkComboBox(self, values=values, width=200)
        self.combobox.set(f"Select {label.lower()[:-1]}")
        self.combobox.configure(state="readonly")
        self.combobox.pack(pady=5)
        return self.combobox
    
    def place_password_entry(self, label):
        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, width=200, show="*")
        self.password_entry.pack(pady=5)
        return self.password_entry

    def place_date_picker(self):
        self.date_picker = DatePicker(self)
        self.master.wait_window(self.date_picker.top)
        selected_date = self.date_picker.get_selected_date()
        if selected_date:
            self.date_of_birth = selected_date
            self.date_of_birth_label.configure(text=f"Date of Birth: {self.date_of_birth}")

    def add_user(self):
        entry_values = self.get_entry_values()

        if not all(entry_values.values()):
            self.alert_var.set("All fields are required!")
            return

        if entry_values["gender"] == "Select gender":
            self.alert_var.set("Please select a valid gender!")
            return

        if entry_values["user_type"] == "Select user type":
            self.alert_var.set("Please select a valid user type!")
            return

        user_type = entry_values.pop("user_type")
        if user_type == "Student":
            entry_values["id"] = f"L{str(uuid.uuid4())[:3].upper()}"
            entry_values["attempted_lessons"] = []
            entry_values["attempted_quizzes"] = []
            if Learner.register(entry_values):
                self.show_success_message("Student")
                self.clear_fields()
            else:
                self.alert_var.set("Failed to add new student!")
        elif user_type == "Admin":
            entry_values["id"] = f"A{str(uuid.uuid4())[:4].upper()}"
            if Admin.register(entry_values):
                self.show_success_message("Admin")
                self.clear_fields()
            else:
                self.alert_var.set("Failed to add new admin!")

    def get_entry_values(self):
        return {
            "username": self.username_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "contact_num": self.contact_num_entry.get(),
            "country": self.country_entry.get(),
            "date_of_birth": self.date_of_birth,
            "gender": self.gender_combobox.get(),
            "password": self.password_entry.get(),
            "profile_picture_path": self.profile_picture_entry.get(),
            "user_type": self.user_type_combobox.get()
        }

    def clear_fields(self):
        for entry in [self.username_entry, self.first_name_entry, self.last_name_entry, 
                      self.contact_num_entry, self.age_entry, self.country_entry, 
                      self.password_entry, self.profile_picture_entry]:
            entry.delete(0, 'end')
        self.gender_combobox.set("Select gender")
        self.user_type_combobox.set("Select user type")
        self.date_of_birth = ""
        self.date_of_birth_label.configure(text="Date of Birth: ")
        self.alert_var.set("")

    def show_success_message(self, user_type):
        CTkMessagebox(title="Success", message=f"{user_type} added successfully!", icon="check")

    def show_page(self):
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_page(self):
        self.pack_forget()

if __name__ == "__main__":
    root = ctk.CTk()
    add_user_page = AdminAddUserPage(root, None)
    root.geometry("800x600")
    add_user_page.pack(expand=True, fill="both")
    root.mainloop()
