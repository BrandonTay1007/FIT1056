import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.quiz import Quiz
from interface.quiz_ui import QuizUI

class QuizList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master)
        self.master = master
        self.user = user
        self.course = course
        self.quizzes = self.load_quizzes()

        self.configure(fg_color="#1E1E1E")
        
        self.create_widgets()
        
    def load_quizzes(self):
        all_quizzes = Quiz.load_all_quizzes()
        return [quiz for quiz in all_quizzes if quiz.associated_course_id == self.course.id]
        
    def create_widgets(self):
        self.quizzes_list_frame = ctk.CTkScrollableFrame(self)
        self.quizzes_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_quiz_bars()
        
    def create_quiz_bars(self):
        if not self.quizzes:
            no_quizzes_label = ctk.CTkLabel(self.quizzes_list_frame, text="No quizzes available", fg_color="#3B3B3B")
            no_quizzes_label.pack(pady=20, fill="x")
            return

        for index, quiz in enumerate(self.quizzes):
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
        self.create_quiz_ui(quiz.id)
        
    def create_quiz_ui(self, quiz_id):
        if not hasattr(self, 'quiz_ui'):
            self.master.quiz_list = self  # Store reference to QuizList
            self.quiz_ui = QuizUI(self.master, quiz_id, self.user, self.on_quiz_complete)
        else:
            self.quiz_ui.pack_forget()
            self.quiz_ui = QuizUI(self.master, quiz_id, self.user, self.on_quiz_complete)
        self.quiz_ui.pack(fill="both", expand=True)

    def on_quiz_complete(self):
        self.hide_page()
        self.master.show_navigation_buttons()
        self.master.show_lessons()
        
    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'quiz_ui'):
            self.quiz_ui.pack_forget()

