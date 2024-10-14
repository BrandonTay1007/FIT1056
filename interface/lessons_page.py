import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from empoweru_constants import LESSONS_FILE_PATH
from sidebar import Sidebar
from app.lessons import Lessons
from app.content import Content
from database.database_management import *

class LessonsPage(ctk.CTkFrame):
    def __init__(self, master, lesson):
        super().__init__(master, fg_color="transparent")
        self.lesson = lesson
        self.sidebar = Sidebar(self.master)
        self.sidebar.show_sidebar()
        self.add_content_to_sidebar()
        self.content_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        
        # Show the first content by default
        if self.lesson.content_list:  # Check if there is any content
            self.show_content(self.lesson.content_list[0])  # Show the first content

    def add_content_to_sidebar(self):
        self.contents = []
        for i, content in enumerate(self.lesson.content_list):
            title = f"{i+1}. {content.title}"
            # Capture the current content in the lambda
            self.sidebar.add_button(title, lambda content=content: self.show_content(content), align="right")

    def show_content(self, content):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Display the content title
        content_title = ctk.CTkLabel(self.content_frame, text=content.title, font=("Roboto", 20, "bold"), pady=10, padx=10)
        content_title.pack(fill="both", expand=True)

        # Display the content text with line wrapping
        content_text = ctk.CTkLabel(self.content_frame, text=content.content, font=("Roboto", 14), wraplength=600)  # Adjust wraplength as needed
        content_text.pack(fill="both", expand=True)

        


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x800")
    lesson_info = get_info_by_id(LESSONS_FILE_PATH, 1)
    lesson_content_list = []
    for content in lesson_info["content_list"]:
        lesson_content_list.append(Content(content["id"], content["title"], content["type"], content["content"]))

    l = Lessons(1, lesson_info["title"], lesson_info["type"], lesson_content_list)
    page = LessonsPage(root, l)
    page.pack(fill="both", expand=True)
    root.mainloop()

