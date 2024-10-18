import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from empoweru_constants import ASSIGNMENTS_FILE_PATH


class Assignment:
    def __init__(self, id, title, due_date, pdf_path, associated_course_id):
        self.id = id
        self.title = title
        self.due_date = due_date
        self.pdf_path = pdf_path
        self.associated_course_id = associated_course_id
        self.submission = None

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
    def init_by_course_id(course_id):
        assignments_data = get_multiple_info_by_id(ASSIGNMENTS_FILE_PATH, "associated_course_id", course_id)
        assignments = []
        for assignment_data in assignments_data:
            assignment = Assignment(
                assignment_data['id'],
                assignment_data['title'],
                assignment_data['due_date'],
                assignment_data['pdf_path'],
                assignment_data['associated_course_id']
            )
            assignments.append(assignment)
        return assignments

    def set_submission(self, submission):
        self.submission = submission

    def get_submission(self):
        return self.submission

    def is_submitted(self):
        return self.submission is not None

    def is_overdue(self, current_date):
        return current_date > self.due_date
