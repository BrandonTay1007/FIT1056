from .user import User

class Learner(User):
    def __init__(self, id, username, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path):
        super().__init__(id, username, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path)
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def drop_course(self, course):
        self.enrolled_courses.remove(course)

    def register(user_data):
        return User.register(user_data)

    
