import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Construct the absolute path to the 'app' directory
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))
sys.path.append(app_path)

from app.course import Course

# Mock constants
LESSONS_FILE_PATH = "mock_lessons_file_path"
COURSES_FILE_PATH = "mock_courses_file_path"

# Mock data
mock_lesson_data = {
    "id": 1,
    "title": "Lesson 1",
    "type": "text",
    "content_list": []
}

mock_course_data = {
    "id": 1,
    "title": "Course 1",
    "estimated_duration": "2 hours",
    "description": "A test course",
    "lessons_id_list": [1]
}

# Mock functions
def mock_get_info_by_id(file_path, key, value):
    if file_path == LESSONS_FILE_PATH and key == "id" and value == 1:
        return mock_lesson_data
    return None

def mock_extract_file_info(file_path):
    if file_path == COURSES_FILE_PATH:
        return [mock_course_data]
    return []

def mock_insert_info(file_path, data):
    pass

# Test cases
@patch('course.get_info_by_id', side_effect=mock_get_info_by_id)
@patch('course.Quiz')
@patch('course.Assignment')
def test_load_lessons(mock_assignment, mock_quiz, mock_get_info):
    mock_quiz.init_by_course_id.return_value = []
    mock_assignment.init_by_course_id.return_value = []

    course = Course("user1", **mock_course_data)
    course.load_lessons()
    
    assert len(course.lessons_list) == 1
    assert course.lessons_list[0].title == "Lesson 1"

@patch('course.insert_info', side_effect=mock_insert_info)
def test_add_course(mock_insert):
    with patch('course.Course.__init__', return_value=None) as mock_init:
        course = Course.add_course(1, "Course 1", "2 hours", "A test course", [1])
        mock_init.assert_called_once_with(1, "Course 1", "2 hours", "A test course", [1])
        mock_insert.assert_called_once()

@patch('course.extract_file_info', side_effect=mock_extract_file_info)
@patch('course.Quiz')
@patch('course.Assignment')
def test_initialize_courses(mock_assignment, mock_quiz, mock_extract):
    mock_quiz.init_by_course_id.return_value = []
    mock_assignment.init_by_course_id.return_value = []

    courses = Course.initialize_courses("user1")
    assert len(courses) == 1
    assert courses[0].title == "Course 1"
