import os
import sys
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class QuizUI(ctk.CTkFrame):
    def __init__(self, master, quiz, user, on_complete_callback):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.on_complete_callback = on_complete_callback

        self.master = master
        self.quiz = quiz
        self.user = user
        self.question_widgets = {}
        self.answers = [None] * len(self.quiz.questions)  # Initialize answers list

        self.create_quiz_page()

    def create_quiz_page(self):
        self.quiz_frame = ctk.CTkScrollableFrame(self, width=480, height=550)
        self.quiz_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        ctk.CTkLabel(self.quiz_frame, text=self.quiz.title, font=("Arial", 20, "bold")).pack(pady=10)

        # Questions
        for i, question in enumerate(self.quiz.questions):
            if question.question_type == "multiple_choice":
                self.add_mcq(i, question)
            else:
                self.add_short_answer(i, question)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_quiz)
        self.submit_button.pack(side="bottom", pady=10)

    def add_mcq(self, index, question):
        frame = ctk.CTkFrame(self.quiz_frame)
        frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(frame, text=f"{index + 1}. {question.question}", wraplength=400).pack(anchor="w")

        var = ctk.StringVar()
        var.trace("w", lambda *args: self.update_answer(index, var.get()))  # Update answer when changed

        for option in question.options:
            ctk.CTkRadioButton(frame, text=option, variable=var, value=option).pack(anchor="w")

        self.question_widgets[index] = frame

    def add_short_answer(self, index, question):
        frame = ctk.CTkFrame(self.quiz_frame)
        frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(frame, text=f"{index + 1}. {question.question}", wraplength=400).pack(anchor="w")

        entry = ctk.CTkEntry(frame, width=300)
        entry.bind("<KeyRelease>", lambda event: self.update_answer(index, entry.get()))  # Update answer when typed
        entry.pack(anchor="w")

        self.question_widgets[index] = frame

    def update_answer(self, index, value):
        self.answers[index] = value

    def submit_quiz(self):
        unanswered = self.answers.count(None)
        if unanswered > 0:
            confirm = CTkMessagebox(
                title="Incomplete Quiz",
                message=f"You have {unanswered} unanswered question(s). Do you want to submit anyway?",
                icon="warning",
                option_1="Go Back",
                option_2="Submit Anyway"
            )
            if confirm.get() == "Go Back":
                return
        else:
            confirm = CTkMessagebox(
                title="Submit Quiz",
                message="Are you sure you want to submit the quiz?",
                icon="question",
                option_1="No",
                option_2="Yes"
            )
            if confirm.get() == "No":
                return

        self.grade_quiz()

    def grade_quiz(self):
        grade, correct = self.quiz.grade_quiz(self.answers)  # Pass answers list to grade_quiz
        self.user.update_grade(self.quiz.id, grade)
        if self.quiz.id not in self.user.attempted_quizzes:
            self.user.update_progress(quiz_id=self.quiz.id)
        # Hide quiz page
        self.quiz_frame.pack_forget()
        self.submit_button.pack_forget()

        # Show grade page
        self.show_grade_page(grade, correct, len(self.quiz.questions))

    def show_grade_page(self, grade, correct, total):
        grade_frame = ctk.CTkFrame(self)
        grade_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(grade_frame, text="Quiz Results", font=("Arial", 24, "bold")).pack(pady=20)
        ctk.CTkLabel(grade_frame, text=f"Your grade: {grade:.2f}%", font=("Arial", 18)).pack(pady=10)
        ctk.CTkLabel(grade_frame, text=f"Correct answers: {correct}/{total}", font=("Arial", 16)).pack(pady=10)

        finish_button = ctk.CTkButton(grade_frame, text="Finish", command=self.on_complete_callback)
        finish_button.pack(pady=10)