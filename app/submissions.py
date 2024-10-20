from database import *
from app.empoweru_constants import *
from datetime import datetime

class Submission:
    def __init__(self, assignment_id, user_id, file_path, submission_date, graded, grade, feedback):
        self.assignment_id = assignment_id
        self.user_id = user_id
        self.file_path = file_path  # This should now be a relative path
        self.submission_date = submission_date
        self.graded = graded
        self.grade = grade
        self.feedback = feedback
    

    def get_username(self):

        user_data = get_info_by_id(LEARNERS_FILE_PATH, "id", self.user_id)
        if user_data:
            return f"{user_data['first_name']} {user_data['last_name']}"
        print(f"User with id {self.user_id} not found")
        return "Unknown User"


    def grade_submission(self):        
        update_data = {
            "feedback": self.feedback,
            "graded": True,
            "grade": self.grade
        }
        
        success = relational_id_update(SUBMISSIONS_FILE_PATH, self.assignment_id, "assignment_id", self.user_id, "user_id", update_data)
        
        if success:
            print(f"Feedback saved successfully for submission assignment {self.assignment_id} and user {self.user_id}")
        else:
            print(f"Failed to save feedback for submission assignment {self.assignment_id} and user {self.user_id}")
        
        return success

    def get_assignment_title(self):
        assignment_data = get_info_by_id(ASSIGNMENTS_FILE_PATH, "id", self.assignment_id)
        return assignment_data["title"]

    def get_submission_date(self):
        return datetime.strptime(self.submission_date, "%Y-%m-%dT%H:%M")

    def get_file_path(self):
        return self.file_path

    def get_file_content(self):
        return read_file_content(self.file_path)

    def get_file_name(self):
        return get_file_name(self.file_path)

    def save_file_content(self, save_path):
        file_content = self.get_file_content()
        if file_content:
            return write_file_content(save_path, file_content)
        return False
