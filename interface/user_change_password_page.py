import customtkinter as ctk
import os
import sys

from app.empoweru_constants import FONT_FAMILY

class ChangePassword(ctk.CTkScrollableFrame):
    def __init__(self, master, user, sidebar):
        super().__init__(master, fg_color="transparent")
        header_label = ctk.CTkLabel(self, text="Password Change", font=(FONT_FAMILY, 24, "bold"))
        header_label.pack(anchor="center", pady=(0, 20))  # Updated to center the header
        self.pack(expand=True, fill="both")
        self.place_all_info() 
        self.user = user
        self.sidebar = sidebar
        self.hide_page()

    def place_all_info(self):
        old_password_label = ctk.CTkLabel(self, text="Old Password:")
        old_password_label.pack(pady=10)
        self.old_password_entry = ctk.CTkEntry(self, show="*")
        self.old_password_entry.pack(pady=10)

        new_password_label = ctk.CTkLabel(self, text="New Password:")
        new_password_label.pack(pady=10)
        self.new_password_entry = ctk.CTkEntry(self, show="*")
        self.new_password_entry.pack(pady=10)

        confirm_password_label = ctk.CTkLabel(self, text="Re-enter New Password:")
        confirm_password_label.pack(pady=10)
        self.confirm_password_entry = ctk.CTkEntry(self, show="*")
        self.confirm_password_entry.pack(pady=10)

        change_password_button = ctk.CTkButton(self, text="Change Password", command=self.change_password)
        change_password_button.pack(pady=10)

        self.alert_var = ctk.StringVar(value="")
        self.alert_label = ctk.CTkLabel(self, textvariable=self.alert_var)
        self.alert_label.pack(pady=10, fill='x', expand=True)  # Updated to fill the width and expand

    def update_alert(self, message, show=True):
        self.alert_var.set(message)
        if show:
            self.alert_label.pack(pady=10)  # Ensure the label is packed when there's an alert
        else:
            self.alert_label.pack_forget()  # Hide the label when there's no alert

    def change_password(self):
        # Check if the new password and confirm password are the same
        if self.new_password_entry.get() != self.confirm_password_entry.get():
            self.update_alert("New password and confirm password do not match")
            return
        else:
            print("New password and confirm password match")
            self.update_alert("", show=False)

        # Check for old password
        if not self.user.check_old_password(self.old_password_entry.get()):
            self.update_alert("Old password is incorrect")
            return
        else:
            print("Old password is correct")
            self.update_alert("", show=False)
        
        result = self.user.change_password(self.new_password_entry.get())
        if result:
            self.update_alert("Password updated successfully")
            self.old_password_entry.delete(0, 'end')
            self.new_password_entry.delete(0, 'end')
            self.confirm_password_entry.delete(0, 'end')
        else:
            self.update_alert("Your password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character")

    def show_page(self):
        self.sidebar.show_sidebar()
        self.pack(expand=True, fill="both")
    
    def hide_page(self):
        self.sidebar.hide_sidebar()
        self.pack_forget()

# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.geometry("800x600")
#     user = Admin("A0001", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing", "Hello Testing")
#     change_password = ChangePassword(root, user)
#     root.mainloop()




