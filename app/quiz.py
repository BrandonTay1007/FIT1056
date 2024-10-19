from app.question import Question
from database import *
from app.empoweru_constants import QUIZZES_FILE_PATH


class Quiz:
    def __init__(self, id, title, questions, associated_course_id):
        self.id = id
        self.title = title
        self.questions = questions
        self.answers = {}
        self.associated_course_id = associated_course_id
        self.current_question_index = 0

    @staticmethod
    def init_by_id(quiz_id):
        questions = []
        quiz_data = get_info_by_id(QUIZZES_FILE_PATH, "id", quiz_id)
        for q in quiz_data['question_list']:
            question = Question(
                q['title'],
                q['selections'],
                q['correct_answer']
            )
            questions.append(question)
        return Quiz(quiz_data['id'], quiz_data['title'], questions, quiz_data['associated_course_id'])

    @staticmethod
    def init_by_course_id(course_id):
        quizzes_data = get_multiple_info_by_id(QUIZZES_FILE_PATH, "associated_course_id", course_id)
        quizzes = []
        for quiz_data in quizzes_data:
            questions = []
            for q in quiz_data['question_list']:
                question = Question(
                    q['title'],
                    q['selections'],
                    q['correct_answer']
                )
                questions.append(question)
            quiz = Quiz(quiz_data['id'], quiz_data['title'], questions, quiz_data['associated_course_id'])
            quizzes.append(quiz)

        return quizzes
    
    @staticmethod
    def load_all_quizzes():
        quizzes_data = extract_file_info(QUIZZES_FILE_PATH)
        quizzes = []
        for quiz_data in quizzes_data:
            questions = []
            for q in quiz_data['question_list']:
                question = Question(
                    q['title'],
                    q['selections'],
                    q['correct_answer']
                )
                questions.append(question)
            quiz = Quiz(quiz_data['id'], quiz_data['title'], questions, quiz_data['associated_course_id'])
            quizzes.append(quiz)

        return quizzes
    
    def set_answer(self, index, answer):
        self.answers[index] = answer

    def get_answer(self, index):
        return self.answers.get(index)

    def get_unanswered_count(self):
        return sum(1 for i in range(len(self.questions)) if not self.get_answer(i))

    def grade_quiz(self, answers):
        correct = 0
        for i, question in enumerate(self.questions):
            if question.check_answer(answers[i]):
                correct += 1

        grade = (correct / len(self.questions)) * 100

        return grade, correct
        
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
        






