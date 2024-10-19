from app.user import User
from app.empoweru_constants import TUTORS_FILE_PATH
from database.database_management import get_info_by_id

class Tutor(User):

    def __init__(self, user_id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender):
        super().__init__(user_id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender)

    def init_by_id(user_id):
        return User.init_by_id(user_id)
    
    @staticmethod
    def _init_from_data(user_data):
        return Tutor(
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
        user_data = get_info_by_id(TUTORS_FILE_PATH, "id", id)
        if user_data is None:
            raise ValueError(f"No tutor found with id: {id}")
        return Tutor._init_from_data(user_data)
    
    @staticmethod
    def init_by_username(username):
        user_data = get_info_by_id(TUTORS_FILE_PATH, "username", username)
        if user_data is None:
            raise ValueError(f"No tutor found with username: {username}")
        return Tutor._init_from_data(user_data)
    
    def register(user_data):
        return User.register(user_data, "tutor")
    
    def update_own_info(self, updated_info, file_path=TUTORS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=TUTORS_FILE_PATH):
        return User.change_password(self, new_password, file_path)


