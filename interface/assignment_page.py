import customtkinter as ctk
import sys
import os
from datetime import datetime
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.assignment import Assignment
from empoweru_constants import FONT_FAMILY

class AssignmentPage(ctk.CTkFrame):
    def __init__(self, master, user, assignment, on_complete_callback):
        super().__init__(master)
        self.master = master
        self.user = user
        self.assignment = assignment
        self.on_complete_callback = on_complete_callback
        
        self.create_widgets()

    def create_widgets(self):
        self.assignment_frame = ctk.CTkScrollableFrame(self, width=480, height=550)
        self.assignment_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        ctk.CTkLabel(self.assignment_frame, text=self.assignment.title, font=(FONT_FAMILY, 20, "bold")).pack(pady=10)

        # Download Question button
        self.download_button = ctk.CTkButton(self.assignment_frame, text="Download Question", command=self.download_question)
        self.download_button.pack(pady=10)

        # Due date
        ctk.CTkLabel(self.assignment_frame, text=f"Due: {self.assignment.due_date}", font=(FONT_FAMILY, 14)).pack(pady=5)

        # Submission status
        status = "Submitted" if self.assignment.is_submitted() else "Not submitted"
        ctk.CTkLabel(self.assignment_frame, text=f"Status: {status}", font=(FONT_FAMILY, 14)).pack(pady=5)

        # File upload button
        self.upload_button = ctk.CTkButton(self.assignment_frame, text="Upload Submission", command=self.upload_file)
        self.upload_button.pack(pady=10)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit Assignment", command=self.submit_assignment)
        self.submit_button.pack(side="bottom", pady=10)

    def get_time_remaining(self, due_date):
        now = datetime.now()
        time_left = due_date - now
        if time_left.total_seconds() <= 0:
            return "Overdue"
        days, seconds = time_left.days, time_left.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def upload_file(self):
        # Implement file upload logic here
        print("File upload functionality to be implemented")

    def submit_assignment(self):
        if not self.assignment.is_submitted():
            confirm = CTkMessagebox(
                title="Submit Assignment",
                message="Are you sure you want to submit the assignment?",
                icon="question",
                option_1="No",
                option_2="Yes"
            )
            if confirm.get() == "Yes":
                # Implement submission logic here
                self.assignment.set_submission(True)  # Assuming a simple boolean for submission status
                self.update_submission_status()
                CTkMessagebox(title="Success", message="Assignment submitted successfully!", icon="check")
                self.on_complete_callback()
        else:
            CTkMessagebox(title="Already Submitted", message="This assignment has already been submitted.", icon="info")

    def update_submission_status(self):
        for widget in self.assignment_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text").startswith("Status:"):
                widget.configure(text="Status: Submitted")
                break

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()

    def download_question(self):
        if not self.assignment.pdf_path:
            CTkMessagebox(title="Error", message="No question file available for this assignment.", icon="cancel")
            return

        # Get the original file name
        original_file_name = os.path.basename(self.assignment.pdf_path)

        # Open file dialog for user to choose save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=os.path.splitext(original_file_name)[1],
            filetypes=[("All Files", "*.*")],
            initialfile=original_file_name
        )

        if file_path:
            try:
                # Check if the source file exists
                if not os.path.exists(self.assignment.pdf_path):
                    raise FileNotFoundError(f"Source file not found: {self.assignment.pdf_path}")

                # Copy the file to the chosen location
                shutil.copy2(self.assignment.pdf_path, file_path)
                CTkMessagebox(title="Success", message="Question file downloaded successfully!", icon="check")
            except FileNotFoundError as e:
                CTkMessagebox(title="Error", message=f"Source file not found. Please contact support.\nDetails: {str(e)}", icon="cancel")
            except PermissionError:
                CTkMessagebox(title="Error", message="Permission denied. Make sure you have the necessary rights to download the file.", icon="cancel")
            except Exception as e:
                CTkMessagebox(title="Error", message=f"Failed to download file: {str(e)}", icon="cancel")
