import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import empoweru_constants as constants

from database.database_management import update_user_info, add_new_user

class User:

    def __init__(self, id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):
        
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num
        self.age = age
        self.country = country
        self.date_of_birth = date_of_birth
        self.gender = gender    
        self.profile_picture_path = profile_picture_path
        

    def authenticate(self, username, password):
        return self.username == username and self.password == password
    
    def __str__(self):
        print(self.first_name)
        print(self.last_name)
        print(self.contact_num)
        print(self.age)
        print(self.country)
        print(self.date_of_birth)
        print(self.gender)

    def get_personal_info(self):

        personal_info = {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_num": self.contact_num,
            "age": self.age,
            "country": self.country,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "profile_picture_path": self.profile_picture_path
        }

        return personal_info
    
    
    def register_new_user(role, user_data):
        return add_new_user(role, user_data)

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

