import customtkinter as ctk
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import get_info_by_id, update_user_info
import empoweru_constants as constants

class EditUserPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master=master

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.master.title("Edit User Page")
        self.master.geometry("600x700")

        #title
        self.title_label=ctk.CTkLabel(self, text="Edit User", font=('Arial', 24, "bold"))
        self.title_label.pack(pady=20)

        #search user
        self.search_user_label=ctk.CTkLabel(self, text="Please enter the user ID to search for:")
        self.search_user_label.pack(pady=10)

        self.search_user_entry=ctk.CTkEntry(self)
        self.search_user_entry.pack()

        self.search_user_button=ctk.CTkButton(self, text="Search", command=self.search_user)
        self.search_user_button.pack(pady=10)

        self.message_label=ctk.CTkLabel(self, text="", font=("Arial", 10))
        self.message_label.pack(pady=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=550, height=400)
        self.scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.save_button=ctk.CTkButton(self, text="Save", command=self.save_edit_info)

        self.user_info_labels=[]
        self.user_info_entries=[]
        self.user_data=None
        self.user_type=None

        self.pack(fill="both", expand=True)

    def search_user(self):
        user_id=self.search_user_entry.get().strip()
        if not user_id:
            self.display_message("Search bar cannot be empty.")
            self.search_user_entry.delete(0, "end")
            self.save_button.pack_forget()
            for label in self.user_info_labels:
                label.destroy()
            for entry in self.user_info_entries:
                entry.destroy()
            return
        
        self.user_data, self.user_type = self.find_user_in_file(user_id)
        
        if self.user_data:
            self.display_message("")
            self.display_user_info()
        else:
            self.display_message("User not found.")
            self.search_user_entry.delete(0, "end")
            self.save_button.pack_forget()
            for label in self.user_info_labels:
                label.destroy()
            for entry in self.user_info_entries:
                entry.destroy()
            return
        
    def find_user_in_file(self, user_id):
        for user_type, file_path in [
            ("admin", constants.ADMIN_FILE_PATH),
            ("tutors", constants.TUTORS_FILE_PATH),
            ("learners", constants.LEARNERS_FILE_PATH)
        ]:
            user_data = get_info_by_id(file_path, user_id)
            if user_data:
                return user_data, user_type
        return None, None

    def display_user_info(self):
        for label in self.user_info_labels:
            label.pack_forget()
        for entry in self.user_info_entries:
            entry.pack_forget()
        self.user_info_labels.clear()
        self.user_info_entries.clear()
        self.save_button.pack_forget()

        variables=["id", "username", "password", "first_name", "last_name", "contact_num", "country", "date_of_birth", "gender", "profile_picture_path"]

        for variable in variables:
            label = ctk.CTkLabel(self.scrollable_frame, text=f"{variable.replace('_', ' ').capitalize()}:")
            label.pack(pady=5)
            entry = ctk.CTkEntry(self.scrollable_frame)
            entry.insert(0, self.user_data.get(variable, ""))
            entry.pack(pady=5)
            self.user_info_labels.append(label)
            self.user_info_entries.append(entry)

        self.save_button.pack(pady=10)

    def save_edit_info(self):
        updated_data = {}
        variables = ["id", "username", "password", "first_name", "last_name", "contact_num", "country", "date_of_birth", "gender", "profile_picture_path"]

        for variable, entry in zip(variables, self.user_info_entries):
            updated_data[variable] = entry.get()

        if self.user_type:
            file_path = self.get_file_path_for_user_type(self.user_type)
            if update_user_info(file_path, updated_data["id"], updated_data):
                self.display_message("User information updated.")
            else:
                self.display_message("Failed to update user information.")

        self.search_user_entry.delete(0, "end")
        self.save_button.pack_forget()
        for label in self.user_info_labels:
            label.destroy()
        for entry in self.user_info_entries:
            entry.destroy()
        
    def get_file_path_for_user_type(self, user_type):
        if user_type == "admin":
            return constants.ADMIN_FILE_PATH
        elif user_type == "tutors":
            return constants.TUTORS_FILE_PATH
        elif user_type == "learners":
            return constants.LEARNERS_FILE_PATH
        else:
            return None

    def display_message(self, message):
        self.message_label.configure(text=message)

    def show_page(self):
        self.pack(expand=True, fill="both")

    def hide_page(self):
        self.pack_forget()

if __name__ == "__main__":
    root=ctk.CTk()
    app=EditUserPage(master=root)
    root.mainloop()
