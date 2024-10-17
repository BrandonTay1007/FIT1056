import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question import Question
from database.database_management import get_info_by_id
from empoweru_constants import QUIZZES_FILE_PATH
class Quiz:
    def __init__(self, title, question_list):
        self.title = title
        self.question_list = question_list
    
    def init_quiz_by_id(id):
        quiz_data = get_info_by_id(QUIZZES_FILE_PATH,id)
        if quiz_data is not None:
            question_list = []
            for question in quiz_data["question_list"]:
                question_list.append(Question(question["number"], question["title"], question["selections"], question["correct_answer"]))
            return Quiz(quiz_data["title"], question_list)
        else:
            return None
        


