import customtkinter as ctk
from tkcalendar import Calendar
from datetime import datetime

class DatePicker:
    def __init__(self, master, default_date=datetime(2010, 1, 1)):
        self.master = master
        self.top = ctk.CTkToplevel(master)
        self.top.title("Date Picker")
        self.top.geometry("300x350")
        
        # Make the date picker window always on top
        self.top.attributes('-topmost', True)
        
        # Disable the parent window while date picker is open
        self.top.grab_set()
        
        self.cal = Calendar(self.top, selectmode='day', date_pattern='dd-mm-yyyy', year=default_date.year, month=default_date.month, day=default_date.day)
        self.cal.pack(pady=20)
        
        # OK button
        ctk.CTkButton(self.top, text="OK", command=self.get_selected_date).pack(pady=10)
        
        self.selected_date = None

    def get_selected_date(self):
        self.selected_date = self.cal.get_date()
        
        # Release the grab before destroying the window
        self.top.grab_release()
        self.top.destroy()
        
        return self.selected_date
    