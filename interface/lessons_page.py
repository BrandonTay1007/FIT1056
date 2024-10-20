import customtkinter as ctk
from app.empoweru_constants import *
from interface.sidebar import Sidebar
from interface.video_player import VideoPlayer

class LessonsPage(ctk.CTkFrame):
    def __init__(self, master, lesson, user):
        super().__init__(master, fg_color="transparent")
        self.master = master
        self.lesson = lesson
        self.user = user
        
        # Initialize sidebar and content frame
        self.sidebar = Sidebar(self.master, 400, 700)
        self.sidebar.show_sidebar()
        self.add_content_to_sidebar()
        self.content_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        
        # Display the first content item by default
        if self.lesson.content_list:
            self.show_content(self.lesson.content_list[0])

    def add_content_to_sidebar(self):
        # Add back button and content list to sidebar
        self.sidebar.add_button("Back", self.go_back, color=None, align="right")
        self.contents = []
        for i, content in enumerate(self.lesson.content_list):
            title = f"{i+1}. {content.title}"
            self.sidebar.add_button(title, lambda content=content: self.show_content(content), align="right")
    
    def show_content(self, content):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if content.type == "video":
            self.create_video_player(content)
        else:
            # Display text content
            content_title = ctk.CTkLabel(self.content_frame, text=content.title, font=(FONT_FAMILY, 20, "bold"), pady=10, padx=10)
            content_title.pack(fill="both", expand=True)

            content_text = ctk.CTkLabel(self.content_frame, text=content.content, font=(FONT_FAMILY, 14), wraplength=600)
            content_text.pack(fill="both", expand=True)

    def create_video_player(self, content):
        # Create and return a video player widget
        return VideoPlayer(self.content_frame, content.title, content.content)

    def hide_page(self):
        # Hide the sidebar and remove the page from view
        self.sidebar.hide_sidebar()
        self.pack_forget()

    def show_page(self):
        # Show the sidebar and display the page
        self.sidebar.show_sidebar()
        self.pack(fill="both", expand=True)

    def go_back(self):
        # Clean up and return to the lessons list
        self.sidebar.hide_sidebar()
        self.sidebar.destroy()
        self.destroy()
        self.master.lessons_list.show_page()
