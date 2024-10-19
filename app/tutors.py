from app.user import User
from empoweru_constants import TEACHERS_FILE_PATH

class Tutor(User):

    def __init__(self, user_id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):
        super().__init__(user_id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path)

    def init_by_id(user_id):
        return User.init_by_id(user_id)
    
    def register(user_data):
        return User.register(user_data, "tutor")
    
    def update_own_info(self, updated_info, file_path=TEACHERS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=TEACHERS_FILE_PATH):
        return User.change_password(self, new_password, file_path)


