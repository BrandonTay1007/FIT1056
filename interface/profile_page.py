import customtkinter as ctk
import os
import sys
import shutil
from tkinter import filedialog
from datetime import datetime
from PIL import Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.admin import Admin
from empoweru_constants import FONT_FAMILY
from interface.date_picker import DatePicker
from interface.sidebar import Sidebar
from interface.change_password_page import ChangePassword

class ProfilePage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        self.user = user
        self.user.profile_page = self
        self.personal_info = user.get_personal_info()
        self.current_active_page = self
        
        # Create a scrollable frame
        self.sidebar = Sidebar(self.master)
        self.sidebar.show_sidebar()
        
        self.change_password = ChangePassword(self.master, self.user)

        # Modify the back button to use go_back method
        self.sidebar.add_button("Back", self.go_back)
        self.sidebar.add_button("Profile", self.go_to_profile)
        self.sidebar.add_button("Change Password", self.go_to_change_password)
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        
        self.current_active_widgets = []
        self.current_date_picker = None  # Add this line to store the current DatePicker instance

        ctk.CTkLabel(self.scrollable_frame, text="Account Details", font=(FONT_FAMILY, 24, "bold")).pack(anchor="w", pady=(0, 20))
        self.place_all_info()
        
    def place_all_info(self):
        items = list(self.personal_info.items())
        for key, value in items:  # Remove the slicing to include all items
            if key != 'profile_picture_path':  # Skip the profile picture path
                self.place_label(key.capitalize().replace("_", " "), value)
        self.add_button("Edit Profile", self.edit_profile)

    def place_all_entry(self):
        self.entry_widgets = {}  # Dictionary to store entry widgets
        
        
        self.entry_widgets['username'] = self.place_entry("Username", self.user.username)
        self.entry_widgets['first_name'] = self.place_entry("First Name", self.user.first_name)
        self.entry_widgets['last_name'] = self.place_entry("Last Name", self.user.last_name)
        self.entry_widgets['contact_num'] = self.place_entry("Contact Number", self.user.contact_num)
        self.entry_widgets['country'] = self.place_entry("Country", self.user.country)
        # Create a frame to hold the date label, date info, and button
        self.date_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.date_frame.pack(anchor="w", pady=(10, 0))

        # Date of Birth label
        date_label = ctk.CTkLabel(self.date_frame, text="Date of Birth")
        date_label.pack(anchor="w", padx=(10, 0))  # Pack the label to the left

        # Create a frame for the date info and button to stack them vertically
        self.date_info_button_frame = ctk.CTkFrame(self.date_frame, fg_color="transparent")
        self.date_info_button_frame.pack(anchor="w", padx=(10, 0))

        # Date info label
        self.date_info = ctk.CTkLabel(self.date_info_button_frame, text=self.user.date_of_birth)
        self.date_info.pack(side="left", padx=(0, 10))  # Pack the date info label to the left

        # Change Date of Birth button
        change_dob_button = ctk.CTkButton(self.date_info_button_frame, text="Change", command=self.place_date_picker)
        change_dob_button.pack(side="left")  # Pack the button to the left
        
        
        self.place_combobox("Gender", ["Male", "Female"])
    

    def hide_widgets(self, widgets_to_hide):
        for widget in widgets_to_hide:
            if widget.winfo_exists():
                widget.pack_forget()
        self.current_active_widgets.clear()
        
        # Hide date-related widgets
        if hasattr(self, 'date_frame'):
            self.date_frame.pack_forget()
        if hasattr(self, 'date_info_button_frame'):
            self.date_info_button_frame.pack_forget()

    def add_button(self, text, command):
        button = ctk.CTkButton(self.scrollable_frame, text=text, command=command)
        button.pack(anchor="w", pady=(10, 0))
        self.current_active_widgets.append(button)

    def place_combobox(self, label, values):
        label_widget = ctk.CTkLabel(self.scrollable_frame, text=label, font=(FONT_FAMILY, 16, "bold"))
        label_widget.pack(anchor="w", pady=(10, 0))
        self.current_active_widgets.append(label_widget)

        self.combobox = ctk.CTkComboBox(self.scrollable_frame, values=values, width=200)
        self.combobox.set(self.user.gender)
        self.combobox.configure(state="readonly")
        self.combobox.pack(anchor="w", pady=(0, 5))
        self.current_active_widgets.append(self.combobox)
    

    def place_label(self, label, label_text, frame=None):
        label_widget = ctk.CTkLabel(frame or self.scrollable_frame, text=label, font=(FONT_FAMILY, 16, "bold"))
        label_widget.pack(anchor="w", pady=(10, 0))
        self.current_active_widgets.append(label_widget)

        text_widget = ctk.CTkLabel(frame or self.scrollable_frame, text=label_text, font=(FONT_FAMILY, 14))
        text_widget.pack(anchor="w", pady=(0, 5))
        self.current_active_widgets.append(text_widget)

    def place_entry(self, label, value, show=None):
        label_widget = ctk.CTkLabel(self.scrollable_frame, text=label, font=(FONT_FAMILY, 16, "bold"))
        label_widget.pack(anchor="w", pady=(10, 0))
        self.current_active_widgets.append(label_widget)

        entry_widget = ctk.CTkEntry(self.scrollable_frame, width=200, font=(FONT_FAMILY, 14), show=show)
        entry_widget.pack(anchor="w", pady=(0, 5))
        entry_widget.insert(0, value)
        self.current_active_widgets.append(entry_widget)
        return entry_widget  # Return the entry widget

    def go_to_change_password(self):
        self.hide_page()
        self.sidebar.show_sidebar()
        self.change_password.show_page()

    def go_to_profile(self):
        self.change_password.hide_page()
        self.show_page()

    def edit_profile(self):
        self.hide_widgets(self.current_active_widgets)
        self.place_all_entry()
        self.add_button("Save Changes", self.save_changes)

    def save_changes(self):
        # Update the personal_info dictionary with new values
        for key, entry_widget in self.entry_widgets.items():
            new_value = entry_widget.get()
            self.personal_info[key] = new_value
        
        # Update the date of birth
        if hasattr(self, 'date_info'):
            new_dob = self.date_info.cget("text")
            self.personal_info['date_of_birth'] = new_dob

        # Update the gender
        if hasattr(self, 'combobox'):
            new_gender = self.combobox.get()
            self.personal_info['gender'] = new_gender

        # Hide all widgets, including date-related ones
        self.hide_widgets(self.current_active_widgets)
    
        # Update the user info and refresh the display
        self.user.update_own_info(self.personal_info)
        self.place_all_info()

    def place_date_picker(self):
        # Destroy any existing DatePicker window
        if self.current_date_picker:
            return
        
        user_dob = datetime.strptime(self.user.date_of_birth, "%d-%m-%Y")
        self.current_date_picker = DatePicker(self.master, user_dob)
        self.master.wait_window(self.current_date_picker.top)
        selected_date = self.current_date_picker.get_selected_date()
        
        if selected_date:
            self.update_date_of_birth_label(selected_date)
        
        self.current_date_picker = None  # Reset the current_date_picker

    def update_date_of_birth_label(self, new_date):
        # Update the label displaying the date of birth
        self.date_info.configure(text=str(new_date))

    def refresh_edit_profile(self):
        self.hide_widgets(self.current_active_widgets)
        self.place_all_entry()
        self.add_button("Save Changes", self.save_changes)

    def show_page(self):
        self.sidebar.show_sidebar()
        self.pack(expand=True, fill="both")

    def hide_page(self):
        self.sidebar.hide_sidebar()
        self.pack_forget()

    def go_back(self):
        self.hide_page()
        self.user.menu.show_page()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("800x600")
    user = Admin("A0001", "CHANGED", "password", "John", "Doe", "0123456789", 20, 
    "Malaysia", "01/01/2000", "Male", "Picture/Default.jpg")
    profile_page = ProfilePage(root, user)
    profile_page.pack(expand=True, fill="both")
    root.mainloop()
