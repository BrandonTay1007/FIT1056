import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import empoweru_constants as constants

from database.database_management import update_user_info, add_new_user

class User:

    def __init__(self, user_id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):

        self.user_id = user_id
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
            "user_id": self.user_id,
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
    
    def validate_user_data(user_data):
        # Username validation
        if not user_data.get("username") or len(user_data["username"]) < 3:
            return False, "Username must be at least 3 characters long"

        # First name and last name validation
        if not user_data.get("first_name") or not user_data.get("last_name"):
            return False, "First name and last name are required"

        # Contact number validation
        if not user_data.get("contact_num") or not user_data["contact_num"].isdigit():
            return False, "Contact number must be a valid number"

        # Age validation
        try:
            age = int(user_data.get("age", 0))
            if age < 13 or age > 120:
                return False, "Age must be between 13 and 120"
        except ValueError:
            return False, "Age must be a valid number"

        # Country validation
        if not user_data.get("country"):
            return False, "Country is required"

        # Date of birth validation
        import datetime
        try:
            dob = datetime.datetime.strptime(user_data.get("date_of_birth", ""), "%Y-%m-%d")
            if dob > datetime.datetime.now():
                return False, "Date of birth cannot be in the future"
        except ValueError:
            return False, "Invalid date of birth format. Use YYYY-MM-DD"

        # Gender validation
        valid_genders = ["Male", "Female", "Other", "Prefer not to say"]
        if user_data.get("gender") not in valid_genders:
            return False, f"Gender must be one of: {', '.join(valid_genders)}"

        # Profile picture path validation (optional)
        if "profile_picture_path" in user_data and not os.path.exists(user_data["profile_picture_path"]):
            return False, "Profile picture path is invalid"

        return True, "All data is valid"
    
    def register_new_user(role, user_data):
        return add_new_user(role, user_data)


    def update_info(self, updated_info):
        personal_info = self.get_personal_info(with_id=True)
        print(personal_info)
        for key, value in updated_info.items():
            try:
                personal_info[key] = value
            except KeyError:
                print(f"KeyError: Key '{key}' not found in personal_info")
        
        if update_user_info(constants.ADMIN_FILE_PATH, self.user_id, personal_info):
            print("User information updated successfully")
            return True

        print("Failed to update user information")
        return False

       


