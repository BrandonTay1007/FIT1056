import customtkinter as ctk
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from interface.date_picker import DatePicker

class AdminEditUserPage(ctk.CTkFrame):

    def __init__(self, master, user):
        super().__init__(master)
        self.master = master
        self.user = user
        self.date_of_birth = ""

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.master.title("Edit User Page")

        #title
        self.title_label = ctk.CTkLabel(self, text="Edit User", font=('Arial', 24, "bold"))
        self.title_label.pack(pady=20)

        #search user
        self.search_user_label = ctk.CTkLabel(self, text="Please enter the user ID to search for:")
        self.search_user_label.pack(pady=10)

        self.search_user_entry = ctk.CTkEntry(self, width=300)  # Increased width to 300
        self.search_user_entry.pack()

        self.search_user_button = ctk.CTkButton(self, text="Search", command=self.search_user)
        self.search_user_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self, text="", font=("Arial", 10))
        self.message_label.pack(pady=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=550, height=300)  # Reduced height to 300
        self.scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_edit_info)

        self.user_info_labels = []
        self.user_info_entries = []
        self.user_data = None

        self.delete_button = ctk.CTkButton(self, text="Delete User", command=self.delete_user, fg_color="red", hover_color="dark red")

        # Add back button
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10, padx=10, anchor="nw")

        self.pack(fill="both", expand=True)

    def search_user(self):
        user_id = self.search_user_entry.get().strip()
        if not user_id:
            self.display_message("Error: Search bar cannot be empty.", "red")
            self.clear_user_info()
            return
        
        if user_id == self.user.id:
            self.display_message("Error: You cannot edit your own account.", "red")
            self.clear_user_info()
            return

        if user_id[0] not in ["A", "T", "L"]:
            self.display_message("Error: Invalid user ID format.", "red")
            self.clear_user_info()
            return

        if user_id[0] == "A":
            self.user_type = "admin"
        elif user_id[0] == "T":
            self.user_type = "tutors"
        elif user_id[0] == "L":
            self.user_type = "learners"

        self.user_data = self.user.get_users_info(user_id, self.user_type)
        print(self.user_data)
        if self.user_data:
            if hasattr(self, 'date_of_birth_label'):
                self.date_of_birth_label.destroy()
            if hasattr(self, 'date_of_birth_button'):
                self.date_of_birth_button.destroy()
            self.display_message("User found successfully.", "green")
            self.display_user_info()
        else:
            self.display_message("Error: User not found.", "red")
            self.search_user_entry.delete(0, "end")
            self.save_button.pack_forget()
            for label in self.user_info_labels:
                label.destroy()
            for entry in self.user_info_entries:
                entry.destroy()
            return
        
    def display_user_info(self):
        for label in self.user_info_labels:
            label.pack_forget()
        for entry in self.user_info_entries:
            entry.pack_forget()
        self.user_info_labels.clear()
        self.user_info_entries.clear()
        self.save_button.pack_forget()

        variables = ["username", "password", "first_name", "last_name", "contact_num", "country", "gender"]
        for variable in variables:
            label = ctk.CTkLabel(self.scrollable_frame, text=f"{variable.replace('_', ' ').capitalize()}:")
            label.pack(pady=5)
            entry = ctk.CTkEntry(self.scrollable_frame)
            entry.insert(0, self.user_data.get(variable, ""))
            entry.pack(pady=5)
            self.user_info_labels.append(label)
            self.user_info_entries.append(entry)

        # Add ID display (non-editable)
        id_label = ctk.CTkLabel(self.scrollable_frame, text=f"User ID: {self.user_data.get('id', '')}")
        id_label.pack(pady=5)
        self.user_info_labels.append(id_label)

        # Add Date of Birth picker
        self.date_of_birth_label = ctk.CTkLabel(self.scrollable_frame, text=f"Date of Birth: {self.user_data.get('date_of_birth', '')}")
        self.date_of_birth_label.pack(pady=5)
        self.date_of_birth_button = ctk.CTkButton(self.scrollable_frame, text="Select Date", command=self.place_date_picker)
        self.date_of_birth_button.pack(pady=5)

        self.save_button.pack(pady=10)
        self.delete_button.pack(pady=10)  # Add this line to display the delete button

    def place_date_picker(self):
        self.date_picker = DatePicker(self)
        self.master.wait_window(self.date_picker.top)
        selected_date = self.date_picker.get_selected_date()
        if selected_date:
            self.date_of_birth = selected_date
            self.date_of_birth_label.configure(text=f"Date of Birth: {self.date_of_birth}")
    
    def delete_user(self):
        if self.user_data and self.user_type:
            if self.user.delete_user(self.user_data["id"], self.user_type):
                self.display_message("User deleted successfully.")
                self.clear_user_info()
            else:
                self.display_message("Failed to delete user.")
        else:
            self.display_message("No user selected.")

    def clear_user_info(self):
        self.search_user_entry.delete(0, "end")
        self.save_button.pack_forget()
        self.delete_button.pack_forget()
        self.user_data = None
        for label in self.user_info_labels:
            label.destroy()
        for entry in self.user_info_entries:
            entry.destroy()
        
        # Clear date of birth elements
        if hasattr(self, 'date_of_birth_label'):
            self.date_of_birth_label.destroy()
        if hasattr(self, 'date_of_birth_button'):
            self.date_of_birth_button.destroy()
        
        # Reset date_of_birth attribute
        self.date_of_birth = ""

        # Clear user_info_labels and user_info_entries lists
        self.user_info_labels.clear()
        self.user_info_entries.clear()

    def validate_edited_data(self, user_data):
        # Create a temporary User object to use for validation
        temp_user = User("", "", "", "", "", "", "", "", "")
        
        # Use the existing register_validation method
        is_valid, error_messages = temp_user.register_validation(user_data)
        
        return is_valid, error_messages

    def save_edit_info(self):
        updated_data = {}
        variables = ["username", "password", "first_name", "last_name", "contact_num", "country", "gender"]

        for variable, entry in zip(variables, self.user_info_entries):
            updated_data[variable] = entry.get()

        # Set date_of_birth to the existing value if it hasn't been changed
        if self.date_of_birth:
            updated_data["date_of_birth"] = self.date_of_birth
        else:
            updated_data["date_of_birth"] = self.user_data.get("date_of_birth", "")

        # Perform validation using the new method
        is_valid, self.error_messages = self.validate_edited_data(updated_data)

        if not is_valid:
            # Display the first error message
            self.display_next_error()
            return

        if self.user_type:
            if self.user.change_user_info(self.user_type, self.user_data["id"], updated_data):
                self.display_message("User information updated.", "green")
            else:
                self.display_message("Failed to update user information.", "red")

    def display_next_error(self):
        if self.error_messages:
            error = self.error_messages.pop(0)
            self.display_message(f"{error}", "red")
        else:
            self.display_message("All errors resolved. You can now save.", "green")
    def display_message(self, message, color="black"):
        self.message_label.configure(text=message, text_color=color)
        self.message_label.lift()  # Bring the message label to the front

    def show_page(self):
        self.pack(expand=True, fill="both")

    def hide_page(self):
        self.pack_forget()

    def go_back(self):
        self.hide_page()
        self.user.menu.show_page()
