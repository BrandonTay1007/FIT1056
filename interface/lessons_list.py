import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.lessons import Lessons
from PIL import Image
import os


class LessonsList(ctk.CTkScrollableFrame):
    def __init__(self, master, user, course_id):
        super().__init__(master, fg_color="transparent")
        
        self.user = user
        lesson_title = ctk.CTkLabel(self, text="Lessons", font=("Arial", 24, "bold"))  # Changed font to Arial, size to 24, and weight to bold
        lesson_title.pack(pady=10)

        # Create a frame to hold the Textbox and Scrollbar
        self.lesson_frame = ctk.CTkFrame(self)
        self.lesson_frame.pack(pady=10)

        # Changed CTkListbox to CTkTextbox
        self.lesson_list = ctk.CTkTextbox(self.lesson_frame, width=200, height=200)  # Changed width and height
        self.lesson_list.pack(side="left", fill="both", expand=True)

        self.lesson_list_scrollbar = ctk.CTkScrollbar(self.lesson_frame, orientation="vertical", command=self.lesson_list.yview)
        self.lesson_list.configure(yscrollcommand=self.lesson_list_scrollbar.set)
        self.lesson_list_scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    root = ctk.CTk()
    lessons_list = LessonsList(root, None)
    lessons_list.pack(fill="both", expand=True)
    root.mainloop()
