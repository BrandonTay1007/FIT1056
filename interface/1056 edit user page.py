import customtkinter as ctk
class EditUserPage(ctk.CTkFrame):

    def __init__(self, master, user: object):
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

        self.save_button=ctk.CTkButton(self, text="Save", command=self.save_edit_info)

        self.user_info_labels=[]
        self.user_info_entries=[]
        self.user_data=None
        self.user_type=None

        self.pack(fill="both", expand=True)

    def search_user(self):
        user=self.search_user_entry.get().strip()
        if not user:
            self.display_message("Search bar cannot be empty.")
            self.search_user_entry.delete(0, "end")
            self.save_button.pack_forget()
            for label in self.user_info_labels:
                label.destroy()
            for entry in self.user_info_entries:
                entry.destroy()
            return
        
        self.user_data=self.find_user_in_file("teacher_user.txt", user)
        if self.user_data:
            self.user_type="Teacher"

        else:
            self.user_data=self.find_user_in_file("student_user.txt", user)
            if self.user_data:
                self.user_type="Student"
            else:
                self.display_message("User not found.")
                self.search_user_entry.delete(0, "end")
                self.save_button.pack_forget()
                for label in self.user_info_labels:
                    label.destroy()
                for entry in self.user_info_entries:
                    entry.destroy()
                return
            
        self.message_label.configure(text="")
        self.display_user_info()
        
    def find_user_in_file(self, file_name, user_id):
        # try:
        #     with open(file_name, "r") as f:
        #         for line in f:
        #             line_data=line.strip().split(",")
        #             if line_data[0].lower()==user_id.lower():
        #                 return line.strip()
        # except FileNotFoundError:
        #         self.display_message(f"{file_name} not found.")
        # return None
        self.user.userlimiandefunction


    def display_user_info(self):
        for label in self.user_info_labels:
            label.pack_forget()
        for entry in self.user_info_entries:
            entry.pack_forget()
        self.user_info_labels.clear()
        self.user_info_entries.clear()
        self.save_button.pack_forget()

        variables=["TeacherID/StudentID", "First Name", "Last Name", "Contact Number", "Instrument"]
        user_info = self.user_data.split(",")

        for i, value in enumerate(user_info):
            label = ctk.CTkLabel(self, text=f"{variables[i]}:")
            label.pack(pady=5)
            self.user_info_labels.append(label)

            entry = ctk.CTkEntry(self)
            entry.insert(0, value)
            entry.pack(pady=5)
            self.user_info_entries.append(entry)

        self.save_button.pack(pady=10)

    def save_edit_info(self):
        updated_data = ','.join(entry.get().strip() for entry in self.user_info_entries)

        file_path = "teacher_user.txt" if self.user_type == "Teacher" else "student_user.txt"
        self.update_user_in_file(file_path, updated_data)

        self.display_message("User information updated.")

        self.search_user_entry.delete(0, "end")
        self.save_button.pack_forget()
        for label in self.user_info_labels:
            label.destroy()
        for entry in self.user_info_entries:
            entry.destroy()
        

    def update_user_in_file(self, file_name, updated_data):
        user_id = self.user_info_entries[0].get().strip()
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()

            with open(file_name, "w") as f:
                for line in lines:
                    if line.startswith(user_id + ","):
                        f.write(updated_data + "\n")
                    else:
                        f.write(line)
        except FileNotFoundError:
            self.display_message(f"{file_name} not found.")

    def display_message(self, message):
        self.message_label.configure(text=message)

if __name__ == "__main__":
    root=ctk.CTk()
    app=EditUserPage(master=root)
    root.mainloop()