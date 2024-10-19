from .user import User
from app.empoweru_constants import LEARNERS_FILE_PATH
from database.database_management import get_info_by_id
class Learner(User):
    def __init__(self, id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender, attempted_lessons, attempted_quizzes):
        super().__init__(id, username, password, first_name, last_name, contact_num, country, date_of_birth, gender)
        self.attempted_lessons = attempted_lessons
        self.attempted_quizzes = attempted_quizzes
    
    @staticmethod
    def _init_from_data(user_data):
        return Learner(
            user_data["id"],
            user_data["username"],
            user_data["password"],
            user_data["first_name"],
            user_data["last_name"],
            user_data["contact_num"],
            user_data["country"],
            user_data["date_of_birth"],
            user_data["gender"],
            user_data["attempted_lessons"],
            user_data["attempted_quizzes"]
        )

    @staticmethod
    def init_by_id(id):
        user_data = get_info_by_id(LEARNERS_FILE_PATH, "id", id)
        if user_data is None:
            raise ValueError(f"No learner found with id: {id}")
        return Learner._init_from_data(user_data)
    
    @staticmethod
    def init_by_username(username):
        user_data = get_info_by_id(LEARNERS_FILE_PATH, "username", username)
        if user_data is None:
            raise ValueError(f"No learner found with username: {username}")
        return Learner._init_from_data(user_data)
    
    def init_by_id(id):
        data = get_info_by_id(LEARNERS_FILE_PATH, "id", id)
        return Learner(data["id"], data["username"], data["password"], data["first_name"], data["last_name"], data["contact_num"], data["country"], data["date_of_birth"], data["gender"], data["attempted_lessons"], data["attempted_quizzes"], data["profile_picture_path"])
    
    def register(user_data):
        user_data["attempted_lessons"] = []
        user_data["attempted_quizzes"] = []
        return User.register(user_data, "learner")

    def update_own_info(self, updated_info, file_path=LEARNERS_FILE_PATH):
        return User.update_own_info(self, updated_info, file_path)

    def change_password(self, new_password, file_path=LEARNERS_FILE_PATH):
        return User.change_password(self, new_password, file_path)


