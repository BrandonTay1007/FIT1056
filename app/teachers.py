from user import User

class Teacher(User):

    def __init__(self, user_id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path="Picture/Default.jpg"):
        super().__init__(user_id, username, password, first_name, last_name, contact_num, age, country, date_of_birth, gender, profile_picture_path)

    def register(user_data):
        return User.register(user_data)