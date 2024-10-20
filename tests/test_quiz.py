import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.question import Question
from database.database_management import *
from app.quiz import Quiz

import pytest

@pytest.fixture
def sample_question_data():
    return {
        'title': 'Which of the following is used to comment a single line in Python?',
        'selections': ['//', '#', '/* */', '--'],
        'correct_answer': '#'
    }

@pytest.fixture
def sample_quiz_data(sample_question_data):
    return {
        'id': 1,
        'title': 'Math Quiz',
        'question_list': [sample_question_data],
        'associated_course_id': 101
    }

@pytest.fixture
def sample_quiz(sample_quiz_data, sample_question_data):
    question = Question(
        sample_question_data['title'],
        sample_question_data['selections'],
        sample_question_data['correct_answer']
    )
    return Quiz(
        sample_quiz_data['id'],
        sample_quiz_data['title'],
        [question],
        sample_quiz_data['associated_course_id']
    )


#Test set and get answer
def test_set_and_get_answer(sample_quiz):
    sample_quiz.set_answer(0, '#')
    assert sample_quiz.get_answer(0) == '#'  
    assert sample_quiz.get_answer(0) != '//' 


# Test count unanswered questions
def test_get_unanswered_count(sample_quiz):
    assert sample_quiz.get_unanswered_count() == 1
    sample_quiz.set_answer(0, '4')
    assert sample_quiz.get_unanswered_count() == 0


#Test grading functionality
def test_grade_quiz(sample_quiz):
    answers = ['#']  # Correct answer
    grade, correct = sample_quiz.grade_quiz(answers)
    assert correct == 1
    assert grade == 100.0

    answers = ['//']  # Incorrect answer
    grade, correct = sample_quiz.grade_quiz(answers)
    assert correct == 0
    assert grade == 0.0


#Test navigating next question
#Test for 1 question only
def test_next_question(sample_quiz):
    assert sample_quiz.next_question() is False 


# Test quiz has question
def test_has_questions(sample_quiz):
    assert sample_quiz.has_questions() is True