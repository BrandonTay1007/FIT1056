import os
import sys
from datetime import datetime
import shutil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from empoweru_constants import ASSIGNMENTS_FILE_PATH, SUBMISSIONS_FILE_PATH
from app.submissions import Submission

class Assignment:
    def __init__(self, user, id, title, due_date, pdf_path, mark, associated_course_id):
        self.user = user
        self.id = id
        self.title = title
        self.due_date = due_date
        self.pdf_path = pdf_path
        self.mark = mark
        self.associated_course_id = associated_course_id
        self.submission = self.check_submission()

    def check_submission(self):
        submission_data = get_multiple_info_by_id(SUBMISSIONS_FILE_PATH, "assignment_id", self.id)
        print(submission_data)
        for submission in submission_data:
            if submission['assignment_id'] == self.id and submission['user_id'] == self.user.id:
                return True
        return False
    
    @staticmethod
    def init_by_id(assignment_id):
        assignment_data = get_info_by_id(ASSIGNMENTS_FILE_PATH, "id", assignment_id)
        return Assignment(
            assignment_data['id'],
            assignment_data['title'],
            assignment_data['due_date'],
            assignment_data['pdf_path'],
            assignment_data['associated_course_id']
        )

    @staticmethod
    def init_by_course_id(user, course_id):
        assignments_data = get_multiple_info_by_id(ASSIGNMENTS_FILE_PATH, "associated_course_id", course_id)
        assignments = []
        for assignment_data in assignments_data:
            assignment = Assignment(
                user,
                assignment_data['id'],
                assignment_data['title'],
                assignment_data['due_date'],
                assignment_data['pdf_path'],
                assignment_data['mark'],
                assignment_data['associated_course_id']
            )
            assignments.append(assignment)
        return assignments

    def set_submission(self, submission):
        self.submission = submission

    def get_submission(self):
        submission_data = get_multiple_info_by_id(SUBMISSIONS_FILE_PATH, "assignment_id", self.id)
        for submission in submission_data:
            if submission['user_id'] == self.user.id:
                return Submission(**submission)
        return None
    
    def get_ungraded_submissions():
        submissions = get_multiple_info_by_id(SUBMISSIONS_FILE_PATH, "graded", False)
        print(submissions)
        return [Submission(**submission) for submission in submissions]

    def submit_file(self, user_id, file_path):
        # Change the submissions folder path
        submissions_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database", "submissions")
        os.makedirs(submissions_folder, exist_ok=True)
        new_file_path = os.path.join(submissions_folder, os.path.basename(file_path))
        shutil.copy2(file_path, new_file_path)

        submission_data = {
            "assignment_id": self.id,
            "user_id": user_id,
            "file_path": new_file_path,
            "submission_date": datetime.now().strftime("%Y-%m-%dT%H:%M"),
            "graded": False,
            "grade": 0,
            "feedback": ""
        }
        
        if insert_info(SUBMISSIONS_FILE_PATH, submission_data):
            self.set_submission(True)
            return True
        return False
