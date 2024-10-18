from typing import List

class Question:
    def __init__(self, question, options, correct_answer, question_type="multiple_choice"):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.question_type = question_type

    def __str__(self):
        return f"Question: {self.question}"

    def check_answer(self, answer):
        if answer is None:
            return False
        
        if self.question_type == "multiple_choice":
            return str(answer).lower().strip() == str(self.correct_answer).lower().strip()
        elif self.question_type == "short_answer":
            # For short answer, we'll check if the answer contains the correct answer
            return str(self.correct_answer).lower().strip() in str(answer).lower().strip()

    

