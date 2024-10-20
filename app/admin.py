from app.user import User
from app.empoweru_constants import ADMIN_FILE_PATH, TUTORS_FILE_PATH, LEARNERS_FILE_PATH
from database import *
class Admin(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender):
        super().__init__(id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender)

    @staticmethod
    def _init_from_data(user_data):
        return Admin(
            user_data["id"],
            user_data["username"],
            user_data["password"],
            user_data["first_name"],
            user_data["last_name"],
            user_data["contact_num"],
            user_data["country"],
            user_data["date_of_birth"],
            user_data["gender"]
        )

    @staticmethod
    def init_by_id(id):
        user_data = get_info_by_id(ADMIN_FILE_PATH, "id", id)
        if user_data is None:
            raise ValueError(f"No admin found with id: {id}")
        return Admin._init_from_data(user_data)
    
    @staticmethod
    def init_by_username(username):
        user_data = get_info_by_id(ADMIN_FILE_PATH, "username", username)
        if user_data is None:
            raise ValueError(f"No admin found with username: {username}")
        return Admin._init_from_data(user_data)

    def register(user_data):
        return User.register(user_data, "admin")

    def register_new_user(self, role, user_data):
        return User.register(role, user_data)
    
    def get_users_info(self, id, role):
        return get_info_by_id(self.get_user_file_path(role), "id", id)

    def get_user_file_path(self, role):
        if role == "admin":
            return ADMIN_FILE_PATH
        elif role == "tutors":
            return TUTORS_FILE_PATH
        elif role == "learners":
            return LEARNERS_FILE_PATH

    def change_user_info(self, role, user_id, new_info):
        return update_info_by_id(self.get_user_file_path(role), 'id', user_id, new_info)

    def delete_user(self, user_id, role):
        file_path = self.get_user_file_path(role)
        return remove_by_id(file_path, user_id)
    
    def update_own_info(self, updated_info, file_path=ADMIN_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=ADMIN_FILE_PATH):
        return User.change_password(self, new_password, file_path)


