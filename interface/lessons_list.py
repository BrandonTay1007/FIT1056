import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.course_content import CourseContent
from PIL import Image
import os


class LessonsList(ctk.CTkFrame):
    def __init__(self, master, lectures):
        super().__init__(master, fg_color="transparent")
        
        self.title_label = ctk.CTkLabel(self, text="Lessons", font=("Roboto", 24, "bold"))
        self.title_label.pack(pady=(20, 10))
        
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.pack(fill="x", padx=20, pady=10)
        
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Search lessons", width=300)
        self.search_entry.pack(side="left")
        
        self.refresh_button = ctk.CTkButton(self.search_frame, text="Refresh", width=100, command=self.refresh_lessons)
        self.refresh_button.pack(side="right")
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.load_lessons()
    
    def create_lesson_bar(self, lesson):
        pass
    
    def load_lessons(self):
        course_content = CourseContent()
        lessons = course_content.get_lessons()
        
        for section in lessons:
            section_label = ctk.CTkLabel(self.scrollable_frame, text=section['title'], font=("Roboto", 18, "bold"))
            section_label.pack(anchor="w", pady=(20, 10))
            
            for lesson in section['lessons']:
                lesson_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
                lesson_frame.pack(fill="x", pady=5)
                
                icon_path = self.get_icon_path(lesson['type'])
                icon_image = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
                icon_label = ctk.CTkLabel(lesson_frame, image=icon_image, text="")
                icon_label.pack(side="left", padx=(0, 10))
                
                check_label = ctk.CTkLabel(lesson_frame, text="✓", text_color="green", font=("Roboto", 16, "bold"))
                check_label.pack(side="left", padx=(0, 10))
                
                lesson_label = ctk.CTkLabel(lesson_frame, text=lesson['title'], anchor="w")
                lesson_label.pack(side="left", fill="x", expand=True)
    
    def get_icon_path(self, lesson_type):
        icon_map = {
            "assignment": "../Pictures/Assignment.png",
            "reading": "../Pictures/Reading.png",
            "video": "../Pictures/Video.png",
            "quiz": "../Pictures/Quiz.png"
        }
        return icon_map.get(lesson_type.lower(), "../Pictures/default_icon.png")
    
    def refresh_lessons(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.load_lessons()


if __name__ == "__main__":
    root = ctk.CTk()
    lessons_list = LessonsList(root)
    lessons_list.pack(fill="both", expand=True)
    root.mainloop()
