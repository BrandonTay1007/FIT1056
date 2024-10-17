import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
from lessons_page import LessonsPage

class LessonsList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master)
        self.master = master
        self.user = user    
        self.course = course
        self.lessons_list = course.lessons_list  # Assuming course has a lesson_list attribute
        print(f"Initializing LessonsList with {len(self.lessons_list)} lessons")
        
        self.configure(fg_color="#1E1E1E")  # Set a dark background color
        
        title_bar = ctk.CTkLabel(self, text=course.title, font=ctk.CTkFont(size=24, weight="bold"))
        title_bar.pack(fill="x", padx=10, pady=10)
        
        self.lessons_list_frame = ctk.CTkScrollableFrame(self)
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_lesson_bars()
        self.create_back_button()
        
    def create_lesson_bars(self):
        if not self.lessons_list:
            no_lessons_label = ctk.CTkLabel(self.lessons_list_frame, text="No lessons available", fg_color="#3B3B3B")
            no_lessons_label.pack(pady=20, fill="x")
            print("No lessons available")
            return

        for index, lesson in enumerate(self.lessons_list):
            lesson_frame = ctk.CTkFrame(self.lessons_list_frame, fg_color="#3B3B3B")
            lesson_frame.pack(fill="x", padx=10, pady=5)

            lesson_label = ctk.CTkLabel(lesson_frame, text=f"{index + 1}. {lesson.title}", anchor="w", fg_color="#3B3B3B")
            lesson_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            view_button = ctk.CTkButton(lesson_frame, text="View", width=80)
            view_button.pack(side="right", padx=10, pady=5)
            # Bind the current lesson using a default argument
            view_button.configure(command=lambda lesson=lesson: self.view_content(lesson))
            
    def view_content(self, lesson):
        self.hide_page()
        self.create_lesson_page(lesson)
        
    def create_lesson_page(self, lesson):
        if not hasattr(self, 'lessons_page'):
            print(f"Creating LessonsPage for lesson: {lesson.title}")
            self.master.lessons_list = self  # Store reference to LessonsList
            self.lessons_page = LessonsPage(self.master, lesson, self.user)
        else:
            self.lessons_page.lesson = lesson
        self.lessons_page.show_page()

    def create_back_button(self):
        back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button_click)
        back_button.pack(side="bottom", padx=10, pady=10, anchor="sw")

    def on_back_button_click(self):
        self.hide_page()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()
        self.user.lecture_selection_page.show_page()

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()

# if __name__ == "__main__":
#     root = ctk.CTk()
#     lessons_list = LessonsList(root, None, 1)
#     lessons_list.pack(fill="both", expand=True)
#     root.mainloop()

