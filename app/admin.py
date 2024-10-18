from app.user import User
from empoweru_constants import ADMIN_FILE_PATH, TUTORS_FILE_PATH, LEARNERS_FILE_PATH
from database.database_management import *
class Admin(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path):
        super().__init__(id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, profile_picture_path)

    def register(user_data):
        return User.register(user_data, "admin")

    def register_new_user(role, user_data):
        return User.register(role, user_data)
    
    def get_users_info(self, id, role):
        if role == "admin":
            return get_info_by_id(ADMIN_FILE_PATH, "id", id)
        elif role == "tutors":
            return get_info_by_id(TUTORS_FILE_PATH, "id", id)
        elif role == "learners":
            return get_info_by_id(LEARNERS_FILE_PATH, "id", id)

    def change_user_info(self, user_id, new_info):
        return User.change_user_info(user_id, new_info)
    
    def delete_user(self, user_id):
        return User.delete_user(user_id)
    
    def update_own_info(self, updated_info, file_path=ADMIN_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=ADMIN_FILE_PATH):
        return User.change_password(self, new_password, file_path)


