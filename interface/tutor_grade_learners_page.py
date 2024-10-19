import customtkinter as ctk
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import os

class TutorGradeLearnersPage(ctk.CTkFrame):
    def __init__(self, master, user, submission):
        super().__init__(master=master)
        self.master = master
        self.user = user
        self.submission = submission
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ctk.CTkLabel(self, text="Grade Submission", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Submission details
        self.details_frame = ctk.CTkFrame(self)
        self.details_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.details_frame, text=f"Learner: {self.submission.get_username()}").pack(anchor="w")
        ctk.CTkLabel(self.details_frame, text=f"Assignment: {self.submission.get_assignment_title()}").pack(anchor="w")
        ctk.CTkLabel(self.details_frame, text=f"Submitted on: {self.submission.get_submission_date()}").pack(anchor="w")

        # Download button
        self.download_button = ctk.CTkButton(self, text="Download Submission", command=self.download_submission)
        self.download_button.pack(pady=10)

        # Grade input
        self.grade_frame = ctk.CTkFrame(self)
        self.grade_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.grade_frame, text="Grade:").pack(side="left", padx=(0, 10))
        self.grade_entry = ctk.CTkEntry(self.grade_frame, width=100)
        self.grade_entry.pack(side="left")
        ctk.CTkLabel(self.grade_frame, text="%").pack(side="left")

        # Feedback input
        self.feedback_label = ctk.CTkLabel(self, text="Feedback:")
        self.feedback_label.pack(anchor="w", padx=20, pady=(10, 5))
        self.feedback_text = ctk.CTkTextbox(self, height=150, width=400)
        self.feedback_text.pack(padx=20, pady=(0, 10), fill="x")

        # Submit grade button
        self.submit_button = ctk.CTkButton(self, text="Submit Grade", command=self.submit_grade)
        self.submit_button.pack(pady=10)

        # Back button
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

        # Error label (initially hidden)
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")

    def download_submission(self):
        file_name = self.submission.get_file_name()
        save_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(file_name)[1],
                                                 filetypes=[("All Files", "*.*")],
                                                 initialfile=file_name)
        if save_path:
            if self.submission.save_file_content(save_path):
                CTkMessagebox(title="Success", message="File downloaded successfully!", icon="check")
            else:
                CTkMessagebox(title="Error", message="Failed to download file.", icon="cancel")

    def submit_grade(self):
        grade = self.grade_entry.get()
        feedback = self.feedback_text.get("1.0", "end-1c")
        
        if not grade:
            self.show_error("Please enter a grade.")
            return

        try:
            grade = float(grade)
            if grade < 0 or grade > 100:
                raise ValueError
        except ValueError:
            self.show_error("Please enter a valid grade between 0 and 100.")
            return

        self.submission.grade = grade
        self.submission.feedback = feedback
        self.submission.grade_submission()
        self.on_grade_return()  # Call the new function after successful grading
        
    def on_grade_return(self):
        # Clear all fields
        self.grade_entry.delete(0, 'end')
        self.feedback_text.delete("1.0", "end")
        self.error_label.configure(text="")
        
        # Refresh the grade list
        self.master.grading_list_page.refresh_submissions_list()
        
        # Show a success message
        CTkMessagebox(title="Success", message="Grade submitted successfully!", icon="check")
        
        # Go back to the grading list page
        self.go_back()

    def go_back(self):
        self.hide_page()
        self.master.grading_list_page.show_page()

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()

    def show_error(self, message):
        self.error_label.configure(text=message)
        self.error_label.pack(pady=(5, 0))
