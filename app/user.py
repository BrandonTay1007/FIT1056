import random
from app.empoweru_constants import *
from database import *

class User:
    def __init__(self, id, username, password, first_name, last_name, 
                 contact_num, country, date_of_birth, gender):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num
        self.country = country
        self.date_of_birth = date_of_birth
        self.gender = gender    
        self.attempted_lessons = []
        self.attempted_quizzes = []
        self.course_list = []

    @classmethod
    def init_by_id(cls, id):
        file_path = {
            'L': LEARNERS_FILE_PATH,
            'T': TUTORS_FILE_PATH,
            'A': ADMIN_FILE_PATH
        }.get(id[0], '')
        
        if not file_path:
            raise ValueError("Invalid user ID")

        data = get_info_by_id(file_path, "id", id)
        return cls(**data)

    @staticmethod
    def authenticate(username, password, file_path):
        user_data = get_info_by_id(file_path, "username", username)
        if user_data and user_data["password"] == password:
            print("User authenticated")
            return True
        return False
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}\n{self.contact_num}\n{self.country}\n{self.date_of_birth}\n{self.gender}"

    def update_grade(self, quiz_id, grade):
        data = {"id": self.id, "quiz_id": quiz_id, "grade": grade}
        relational_id_update(GRADES_FILE_PATH, self.id, "id", quiz_id, "quiz_id", data)

    def get_personal_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_num": self.contact_num,
            "country": self.country,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender
        }

    @staticmethod
    def register(user_data, role):
        role = role.lower()
        file_path = {
            "learner": LEARNERS_FILE_PATH,
            "tutor": TUTORS_FILE_PATH,
            "admin": ADMIN_FILE_PATH
        }.get(role)

        if not file_path:
            raise ValueError("Invalid role")

        id_prefix = {"learner": "L", "tutor": "T", "admin": "A"}[role]
        existing_ids = extract_file_info(file_path)
        
        while True:
            new_id = f"{id_prefix}{str(random.randint(1, 9999)).zfill(4)}"
            if new_id not in [user["id"] for user in existing_ids]:
                break
        
        user_data["id"] = new_id
        if insert_info(file_path, user_data):
            print(f"User registered successfully with ID: {new_id}")
            return True
        print(f"Failed to register user with ID: {new_id}")
        return False

    @staticmethod
    def name_validation(first_name, last_name):
        if not first_name.strip() or not last_name.strip():
            print("Name cannot be empty")
            return False
        return True

    @staticmethod
    def contact_num_validation(contact_num):
        if not contact_num.isdigit():
            print("Contact number must be digits")
            return False
        if len(contact_num) != 10:
            print("Contact number must be 10 digits")
            return False
        return True

    def register_validation(self, user_data):
        is_valid = True
        error_messages = []

        validations = [
            (len(user_data["username"]) < 4, "Username must be at least 4 characters long"),
            (not self.name_validation(user_data["first_name"], user_data["last_name"]), "Names should contain only letters and spaces"),
            (not self.contact_num_validation(user_data["contact_num"]), "Contact number must be 10 digits"),
            (not user_data["country"].replace(" ", "").isalpha(), "Country should contain only letters and spaces"),
            (not user_data["date_of_birth"], "Date of birth is required"),
            (user_data["gender"] == "Select your gender", "Please select a valid gender"),
            (not self.password_validation(user_data["password"]), "Password must be at least 8 characters long, contain uppercase and lowercase letters, digits, and special characters")
        ]

        for validation, error_message in validations:
            if validation:
                error_messages.append(error_message)
                is_valid = False

        return is_valid, error_messages
    
    def update_own_info(self, updated_info, file_path):
        personal_info = self.get_personal_info()
        for key, value in updated_info.items():
            try:
                personal_info[key] = value
            except KeyError:
                print(f"KeyError: Key '{key}' not found in personal_info")

        if update_info_by_id(file_path, 'id', self.id, personal_info):
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

        if update_info_by_id(file_path, 'id', self.id, {"password": new_password}):
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
        
        update_info_by_id(LEARNERS_FILE_PATH, 'id', self.id, {"attempted_lessons": self.attempted_lessons, "attempted_quizzes": self.attempted_quizzes})
        
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
        
    def get_all_assignments(self):
        assignments = []
        for course in self.course_list:
            for assignment in course.assignments:
                submission = assignment.get_submission()
                if submission and submission.graded:
                    assignments.append({
                        'title': assignment.title,
                        'grade': submission.grade,
                        'course_title': course.title
                    })
        return assignments
