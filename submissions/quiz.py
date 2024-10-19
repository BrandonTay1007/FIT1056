import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .question import Question
from database.database_management import get_info_by_id
from empoweru_constants import QUIZZES_FILE_PATH
import json
from typing import List


class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.current_question_index = 0

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        quizzes = []
        for quiz_data in data:
            questions = []
            for q in quiz_data['questions']:
                question = Question(
                    q['question'],
                    q.get('options', []),
                    q['correct_answer'],
                    q.get('question_type', 'multiple_choice')
                )
                questions.append(question)
            quiz = cls(quiz_data['title'], questions)
            quizzes.append(quiz)
        
        return quizzes

    def get_current_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return True
        return False

    def has_questions(self):
        return len(self.questions) > 0

    # ... rest of the class methods ...
        




