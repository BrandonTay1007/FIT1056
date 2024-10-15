from app.user import User
from empoweru_constants import ADMIN_FILE_PATH
class Admin(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path):
        super().__init__(id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path)

    def register(user_data):
        return User.register(user_data)

    def get_users_info(self):
        return User.get_users_info()
    
    def change_user_info(self, user_id, new_info):
        return User.change_user_info(user_id, new_info)
    
    def delete_user(self, user_id):
        return User.delete_user(user_id)
    
    def update_own_info(self, updated_info, file_path=ADMIN_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=ADMIN_FILE_PATH):
        return User.change_password(self, new_password, file_path)


