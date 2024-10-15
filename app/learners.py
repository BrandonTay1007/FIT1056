from .user import User
from empoweru_constants import LEARNERS_FILE_PATH

class Learner(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path):
        super().__init__(id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path)
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def drop_course(self, course):
        self.enrolled_courses.remove(course)

    def register(user_data):
        return User.register(user_data)

    def update_own_info(self, updated_info, file_path=LEARNERS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=LEARNERS_FILE_PATH):
        return User.change_password(self, new_password, file_path)


