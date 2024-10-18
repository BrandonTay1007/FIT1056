from .user import User
from empoweru_constants import LEARNERS_FILE_PATH

class Learner(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, attempted_lessons, attempted_quizzes, profile_picture_path):
        super().__init__(id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path)
        self.attempted_lessons = attempted_lessons
        self.attempted_quizzes = attempted_quizzes
        
    def register(user_data):
        return User.register(user_data)

    def update_own_info(self, updated_info, file_path=LEARNERS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=LEARNERS_FILE_PATH):
        return User.change_password(self, new_password, file_path)


