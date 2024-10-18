import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from empoweru_constants import *
from app.quiz import Quiz
from database.database_management import *

class User:

    def __init__(self, id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):
        
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num
        self.country = country
        self.date_of_birth = date_of_birth
        self.gender = gender    
        self.profile_picture_path = profile_picture_path
    
    def init_by_id(id):
        data = get_info_by_id(LEARNERS_FILE_PATH, "id", id)
        return User(data["id"], data["username"], data["password"], data["first_name"], data["last_name"], data["contact_num"], data["country"], data["date_of_birth"], data["gender"], data["profile_picture_path"])
    
    def authenticate(self, username, password):
        return self.username == username and self.password == password
    
    def __str__(self):
        print(self.first_name)
        print(self.last_name)
        print(self.contact_num)
        print(self.country)
        print(self.date_of_birth)
        print(self.gender)

    def update_grade(self, quiz_id, grade):
        data = {
            "id": self.id,
            "quiz_id": quiz_id,
            "grade": grade
        }
        relational_id_update(GRADES_FILE_PATH, self.id, quiz_id, data)

    def get_personal_info(self):

        personal_info = {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_num": self.contact_num,
            "country": self.country,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "profile_picture_path": self.profile_picture_path
        }

        return personal_info
    
    def register(role, user_data):
        if role == "learner":
            file_path = LEARNERS_FILE_PATH
        elif role == "tutor":
            file_path = TUTORS_FILE_PATH
        elif role == "admin":
            file_path = ADMIN_FILE_PATH
        
        return insert_info(file_path, user_data)

    def update_own_info(self, updated_info, file_path):
        personal_info = self.get_personal_info()
        for key, value in updated_info.items():
            try:
                personal_info[key] = value
            except KeyError:
                print(f"KeyError: Key '{key}' not found in personal_info")

        if update_user_info(file_path, self.id, personal_info):
            print("User information updated successfully")
            return True

        print("Failed to update user information")
        return False
    
    def password_validation(self, password):
        if not (len(password) > 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()_+{}[]:<>?~" for char in password)):
            return False
        return True
    
    def check_old_password(self, old_password):
        print(self.password)
        return self.password == old_password
    
    def change_password(self, new_password, file_path):
        is_valid = self.password_validation(new_password)
        if not is_valid:
            return is_valid

        if update_user_info(file_path, self.id, {"password": new_password}):
            print("Password updated successfully")
            return True
        print("Failed to update password")
        return False

    def update_progress(self, lessons_id=None, quiz_id=None):
        if lessons_id:
            if lessons_id not in self.attempted_lessons:
                self.attempted_lessons.append(lessons_id)

        if quiz_id:
            if quiz_id not in self.attempted_quizzes:
                self.attempted_quizzes.append(quiz_id)
        
        update_user_info(LEARNERS_FILE_PATH, self.id, {"attempted_lessons": self.attempted_lessons, "attempted_quizzes": self.attempted_quizzes})
        
    def get_all_grades(self):
        user_grades = get_multiple_info_by_id(GRADES_FILE_PATH, "id", self.id)
        grades = []
        for grade in user_grades:
            for course in self.course_list:
                for quiz in course.quizzes:
                    if quiz.id == grade['quiz_id']:
                        grade['quiz_title'] = quiz.title
                        grade['quiz_id'] = quiz.id
                        grade['course_title'] = course.title
                        grades.append(grade)
        
        return grades
        