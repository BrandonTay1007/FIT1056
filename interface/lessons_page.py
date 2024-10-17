import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from empoweru_constants import LESSONS_FILE_PATH
from sidebar import Sidebar
from empoweru_constants import *
from video_player import VideoPlayer

class LessonsPage(ctk.CTkFrame):
    def __init__(self, master, lesson, user):
        super().__init__(master, fg_color="transparent")
        self.master = master
        self.lesson = lesson
        self.user = user
        self.sidebar = Sidebar(self.master, 400, 700)
        self.sidebar.show_sidebar()
        self.add_content_to_sidebar()
        self.content_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        
        # Show the first content by default
        if self.lesson.content_list:
            print("OK")  # Check if there is any content
            self.show_content(self.lesson.content_list[0])  # Show the first content

    def add_content_to_sidebar(self):
        self.sidebar.add_button("Back", self.go_back, color=None, align="right")
        self.contents = []
        for i, content in enumerate(self.lesson.content_list):
            title = f"{i+1}. {content.title}"
            # Capture the current content in the lambda
            self.sidebar.add_button(title, lambda content=content: self.show_content(content), align="right")
        
    
    def show_content(self, content):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Check if the content is a video
        if content.type == "video":
            self.create_video_player(content)
        else:
            # Display the content title
            content_title = ctk.CTkLabel(self.content_frame, text=content.title, font=(FONT_FAMILY, 20, "bold"), pady=10, padx=10)
            content_title.pack(fill="both", expand=True)

            # Display the content text with line wrapping
            content_text = ctk.CTkLabel(self.content_frame, text=content.content, font=(FONT_FAMILY, 14), wraplength=600)  # Adjust wraplength as needed
            content_text.pack(fill="both", expand=True)

    def create_video_player(self, content):
        # Create a video player widget using Tkvideoplayer
        video_player = VideoPlayer(self.content_frame, content.title, content.content)  # Load the video from the provided URL
        return video_player  # Return the video player instance

    def hide_page(self):
        self.sidebar.hide_sidebar()
        self.pack_forget()

    def show_page(self):
        self.sidebar.show_sidebar()
        self.pack(fill="both", expand=True)

    def go_back(self):
        self.sidebar.hide_sidebar()
        self.hide_page()
        self.master.lessons_list.show_page()


# from app.content import Content
# from database.database_management import get_info_by_id
# from app.lessons import Lessons

# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.geometry("1200x800")
#     lesson_info = get_info_by_id(LESSONS_FILE_PATH, 1)
#     lesson_content_list = []
#     for content in lesson_info["content_list"]:
#         print(content)
#         lesson_content_list.append(Content(content["id"], content["title"], content["type"], content["content"]))

#     l = Lessons(1, lesson_info["title"], lesson_info["type"], lesson_content_list)
#     page = LessonsPage(root, l)
#     page.pack(fill="both", expand=True)
#     root.mainloop()
