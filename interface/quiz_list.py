import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.quiz_ui import QuizUI
from interface.assignment_list import AssignmentList  # Import the new AssignmentList

class QuizList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master)
        self.master = master
        self.user = user
        self.course = course
        self.course_quiz = course.quizzes
        self.configure(fg_color="#1E1E1E")
        self.create_widgets()
        
    def create_widgets(self):
        self.quizzes_list_frame = ctk.CTkScrollableFrame(self)
        self.quizzes_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_quiz_bars()
        
    def create_quiz_bars(self):
        if not self.course_quiz:
            no_quizzes_label = ctk.CTkLabel(self.quizzes_list_frame, text="No quizzes available", fg_color="#3B3B3B")
            no_quizzes_label.pack(pady=20, fill="x")
            return

        for index, quiz in enumerate(self.course_quiz):
            quiz_frame = ctk.CTkFrame(self.quizzes_list_frame, fg_color="#3B3B3B")
            quiz_frame.pack(fill="x", padx=10, pady=5)

            quiz_label = ctk.CTkLabel(quiz_frame, text=f"{index + 1}. {quiz.title}", anchor="w", fg_color="#3B3B3B")
            quiz_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            start_button = ctk.CTkButton(quiz_frame, text="Start", width=80)
            start_button.pack(side="right", padx=10, pady=5)
            start_button.configure(command=lambda q=quiz: self.start_quiz(q))
            
    def start_quiz(self, quiz):
        self.master.hide_navigation_buttons()
        self.master.hide_back_button()
        self.hide_page()
        self.create_quiz_ui(quiz)
        
    def create_quiz_ui(self, quiz):
        if not hasattr(self, 'quiz_ui'):
            self.master.quiz_list = self  # Store reference to QuizList
            self.quiz_ui = QuizUI(self.master, quiz, self.user, self.on_quiz_complete)
        else:
            self.quiz_ui.pack_forget()
            self.quiz_ui = QuizUI(self.master, quiz, self.user, self.on_quiz_complete)
        self.quiz_ui.pack(fill="both", expand=True)

    def on_quiz_complete(self):
        self.hide_page()
        self.master.show_navigation_buttons()
        self.master.show_quizzes()
        self.master.show_back_button()
        
    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'quiz_ui'):
            self.quiz_ui.pack_forget()

    def create_navigation_buttons(self):
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.lessons_button = ctk.CTkButton(self.button_frame, text="Lessons", command=self.show_lessons)
        self.lessons_button.pack(side="left", padx=(0, 5))
        
        self.quizzes_button = ctk.CTkButton(self.button_frame, text="Quizzes", command=self.show_quizzes)
        self.quizzes_button.pack(side="left", padx=(5, 0))
        
        self.assignments_button = ctk.CTkButton(self.button_frame, text="Assignments", command=self.show_assignments)
        self.assignments_button.pack(side="left", padx=(5, 0))

    def show_lessons(self):
        self.hide_page()
        if hasattr(self.master, 'assignment_list'):
            self.master.assignment_list.hide_page()
        self.master.show_lessons()

    def show_quizzes(self):
        self.show_page()
        if hasattr(self.master, 'assignment_list'):
            self.master.assignment_list.hide_page()

    def show_assignments(self):
        self.hide_page()
        if not hasattr(self.master, 'assignment_list'):
            self.master.assignment_list = AssignmentList(self.master, self.user, self.course)
        self.master.assignment_list.show_page()

    def hide_navigation_buttons(self):
        self.button_frame.pack_forget()

    def show_navigation_buttons(self):
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)
