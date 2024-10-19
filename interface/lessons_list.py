import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
from interface.lessons_page import LessonsPage
from interface.quiz_list import QuizList
from interface.assignment_list import AssignmentList
class LessonsList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master)
        self.master = master
        self.user = user    
        self.course = course
        self.lessons_list = course.lessons_list
        
        self.configure(fg_color="#1E1E1E")
        
        self.create_widgets()
        
    def create_widgets(self):
        title_bar = ctk.CTkLabel(self, text=self.course.title, font=ctk.CTkFont(size=24, weight="bold"))
        title_bar.pack(fill="x", padx=10, pady=10)
        
        self.lessons_list_frame = ctk.CTkScrollableFrame(self)
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_lesson_bars()
        self.create_back_button()
        self.create_navigation_buttons()
        
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
            view_button.configure(command=lambda lesson=lesson: self.view_content(lesson))
            
    def view_content(self, lesson):
        self.hide_page()
        self.create_lesson_page(lesson)
        if str(lesson.id) not in self.user.attempted_lessons:
            self.user.update_progress(lessons_id=lesson.id)
        
    def create_lesson_page(self, lesson):
        if not hasattr(self, 'lessons_page'):
            print(f"Creating LessonsPage for lesson: {lesson.title}")
            self.master.lessons_list = self  # Store reference to LessonsList
            self.lessons_page = LessonsPage(self.master, lesson, self.user)
        else:
            self.lessons_page.lesson = lesson
        self.lessons_page.show_page()

    def create_back_button(self):
        self.back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button_click)
        self.back_button.pack(side="bottom", padx=10, pady=10, anchor="sw")

    def on_back_button_click(self):
        self.hide_page()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()
        self.user.lecture_selection_page.show_page()
        self.user.lecture_selection_page.progress_tracker.init_progress()
    
    def show_page(self):
        self.pack(fill="both", expand=True)
        self.show_back_button()

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()

    def create_navigation_buttons(self):
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.lessons_button = ctk.CTkButton(self.button_frame, text="Lessons", command=self.show_lessons)
        self.lessons_button.pack(side="left", padx=(0, 5))
        
        self.quizzes_button = ctk.CTkButton(self.button_frame, text="Quizzes", command=self.show_quizzes)
        self.quizzes_button.pack(side="left", padx=(5, 0))
        
        self.assignments_button = ctk.CTkButton(self.button_frame, text="Assignments", command=self.show_assignments)
        self.assignments_button.pack(side="left", padx=(5, 0))

        self.update_nav_buttons("lessons")  # Set initial active button

    def update_nav_buttons(self, active_page):
        active_color = "#1E90FF"  # Dodger Blue
        inactive_color = "#3B3B3B"  # Dark gray

        self.lessons_button.configure(fg_color=active_color if active_page == "lessons" else inactive_color)
        self.quizzes_button.configure(fg_color=active_color if active_page == "quizzes" else inactive_color)
        self.assignments_button.configure(fg_color=active_color if active_page == "assignments" else inactive_color)

    def show_lessons(self):
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        if hasattr(self, 'quiz_list'):
            self.quiz_list.pack_forget()
        if hasattr(self, 'assignment_list'):
            self.assignment_list.hide_page()
        self.show_back_button()
        self.update_nav_buttons("lessons")
        
    def show_quizzes(self):
        self.lessons_list_frame.pack_forget()
        if hasattr(self, 'assignment_list'):
            self.assignment_list.hide_page()
        if not hasattr(self, 'quiz_list'):
            self.quiz_list = QuizList(self, self.user, self.course)
        self.quiz_list.pack(fill="both", expand=True)
        self.update_nav_buttons("quizzes")

    def show_assignments(self):
        self.lessons_list_frame.pack_forget()
        if hasattr(self, 'quiz_list'):
            self.quiz_list.pack_forget()
        if not hasattr(self, 'assignment_list'):
            self.assignment_list = AssignmentList(self, self.user, self.course)
        self.assignment_list.show_page()
        self.update_nav_buttons("assignments")

    def hide_navigation_buttons(self):
        self.button_frame.pack_forget()

    def show_navigation_buttons(self):
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    def hide_back_button(self):
        self.back_button.pack_forget()

    def show_back_button(self):
        self.back_button.pack(side="bottom", padx=10, pady=10, anchor="sw")
# if __name__ == "__main__":
#     root = ctk.CTk()
#     lessons_list = LessonsList(root, None, 1)
#     lessons_list.pack(fill="both", expand=True)
#     root.mainloop()
