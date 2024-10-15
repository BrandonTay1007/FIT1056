import customtkinter as ctk
import app.Admin as 
class AdminAddUserPage(ctk.CTkScrollableFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.title = ctk.CTkLabel(master=self, text="Add User", font=("Roboto", 30))
        self.title.grid(row=0, column=1, padx=10, pady=20)

        self.add_dropdown()

        self.add_entry(2, 1, "Username")
        self.add_entry(3, 1, "Password")
        self.add_entry(4, 1, "First Name")
        self.add_entry(5, 1, "Last Name")
        self.add_entry(6, 1, "Contact Number")
        self.add_entry(7, 1, "Age")
        self.add_entry(8, 1, "Country")
        self.add_entry(9, 1, "Date of Birth")
        self.add_entry(10, 1, "Gender")

    def select_role(self, role):
        self.selected_role = role
        self.refresh_form()

    def add_user(self):
        pass

    def add_dropdown(self):
        self.user_type = ctk.CTkOptionMenu(
            master=self,
            values=["Student", "Tutor", "Admin"],
            command=self.select_role,  # Add this line to set the command
            width=200,
            height=40
        )
        self.user_type.set("Select User Type")
        self.user_type.grid(row=1, column=1, pady=10)

    def add_entry(self, row, column, placeholder):
        entry = ctk.CTkEntry(master=self, placeholder_text=placeholder, width=200, height=40)
        entry.grid(row=row, column=column, pady=10)

    def refresh_form(self):
        if self.selected_role == "Student":
            self.add_student_form()
        elif self.selected_role == "Tutor":
            self.add_tutor_form()
        elif self.selected_role == "Admin":
            self.add_admin_form()
        
    def add_student():
        user

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x800")
    my_admin = admin.Admin("JohnDoe", "Passwordx", "firstname", "lastname", "contactnum", "age", "country", "dateofbirth", "gender", "profilepicturepath")
    page = AdminAddUserPage(root, my_admin)
    page.pack(fill="both", expand=True)
    root.mainloop()
