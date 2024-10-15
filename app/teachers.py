from user import User
from empoweru_constants import TEACHERS_FILE_PATH

class Teacher(User):

    def __init__(self, user_id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):
        super().__init__(user_id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path)

    def register(user_data):
        return User.register(user_data)
    
    def update_own_info(self, updated_info, file_path=TEACHERS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)
