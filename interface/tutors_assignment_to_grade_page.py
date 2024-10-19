import customtkinter as CTk
from app.assignment import Assignment
from interface.tutor_grade_learners_page import TutorGradeLearnersPage

class GradingListPage(CTk.CTkFrame):
    def __init__(self, master, tutors):
        super().__init__(master)
        self.tutors = tutors
        self.ungraded_submissions = self.get_sorted_submissions()
        self.create_widgets()
    
    def get_sorted_submissions(self):
        submissions = Assignment.get_ungraded_submissions()
        return sorted(submissions, key=lambda x: x.submission_date, reverse=True)
    
    def create_widgets(self):
        # Create a scrollable frame
        if not hasattr(self, "scrollable_frame"):
            self.scrollable_frame = CTk.CTkScrollableFrame(self, width=780, height=580)  # Increased height
            self.scrollable_frame.pack(padx=10, pady=10, expand=True, fill="both")

        # Create headers
        headers = ["User ID", "Name", "Assignment Title", "Submission Date", "Action"]
        for col, header in enumerate(headers):
            CTk.CTkLabel(self.scrollable_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=5, pady=5, sticky="w")

        # Create list items
        for row, submission in enumerate(self.ungraded_submissions, start=1):
            CTk.CTkLabel(self.scrollable_frame, text=str(submission.user_id)).grid(row=row, column=0, padx=5, pady=2, sticky="w")
            CTk.CTkLabel(self.scrollable_frame, text=submission.get_username()).grid(row=row, column=1, padx=5, pady=2, sticky="w")
            CTk.CTkLabel(self.scrollable_frame, text=submission.get_assignment_title()).grid(row=row, column=2, padx=5, pady=2, sticky="w")
            CTk.CTkLabel(self.scrollable_frame, text=submission.get_submission_date()).grid(row=row, column=3, padx=5, pady=2, sticky="w")
            
            CTk.CTkButton(self.scrollable_frame, text="View", command=lambda s=submission: self.view_submission(s)).grid(row=row, column=4, padx=5, pady=2)

        # Add a back button at the bottom left
        self.back_button = CTk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.pack(side="bottom", anchor="sw", padx=10, pady=10)

    def refresh_submissions_list(self):
        self.ungraded_submissions = self.get_sorted_submissions()
        # Destroy old widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_widgets()
        
    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()

    def view_submission(self, submission):
        self.hide_page()
        self.master.grading_list_page = self
        if not hasattr(submission, "tutor_grade_learners_page"):
            submission.tutor_grade_learners_page = TutorGradeLearnersPage(self.master, self.tutors, submission)
        submission.tutor_grade_learners_page.show_page()

    def go_back(self):
        self.hide_page()
        self.tutors.menu.show_page()
