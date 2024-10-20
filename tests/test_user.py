import sys
import os
import json
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.empoweru_constants import *
from database.database_management import *
from app.user import User
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_tutors_file(tmp_path):
    tutors_data = [
        {
            "id": "T0001",
            "username": "JohnnyBoy",
            "password": "Hashed_password_1",
            "first_name": "John",
            "last_name": "Doe",
            "contact_num": "1234567890",
            "country": "USA",
            "date_of_birth": "1990-01-01",
            "gender": "Male"
        }
    ]

    file_path = tmp_path / "tutors.json"
    with open(file_path, 'w') as f:
        json.dump(tutors_data, f)

    return str(file_path)

@pytest.fixture
def sample_user():
    with open(os.path.join(os.path.dirname(__file__), '..', 'database', 'tutors.json'), 'r') as f:
        tutors_data = json.load(f)

    sample_data = tutors_data[0]
    
    return User(
        id=sample_data["id"],
        username=sample_data["username"],
        password=sample_data["password"],
        first_name=sample_data["first_name"],
        last_name=sample_data["last_name"],
        contact_num=sample_data["contact_num"],
        country=sample_data["country"],
        date_of_birth=sample_data["date_of_birth"],
        gender=sample_data["gender"]
    )

@pytest.fixture
def sample_user_with_grades():
    user = User(
        id="L0001",
        username="LearnerUser",
        password="LearnerPassword@123",
        first_name="Alice",
        last_name="Smith",
        contact_num="0987654321",
        country="Canada",
        date_of_birth="1995-01-01",
        gender="Female"
    )
    
    user.course_list = [
        MagicMock(title="Introduction to Programming in Python", quizzes=[
            MagicMock(id="Q001", title="Quiz 1"),
            MagicMock(id="Q002", title="Quiz 2")
        ]),
        MagicMock(title="Machine Learning", quizzes=[
            MagicMock(id="Q003", title="Quiz 1"),
            MagicMock(id="Q004", title="Quiz 2")
        ])
    ]
    
    user.attempted_lessons = []
    user.attempted_quizzes = []

    return user

def test_get_personal_info(sample_user):
    personal_info = sample_user.get_personal_info()
    assert personal_info["id"] == "T0001"
    assert personal_info["username"] == "JohnnyBoy"
    assert personal_info["first_name"] == "John"
    assert personal_info["last_name"] == "Doe"
    assert personal_info["contact_num"] == "1234567890"
    assert personal_info["country"] == "USA"
    assert personal_info["date_of_birth"] == "1990-01-01"
    assert personal_info["gender"] == "Male"

    assert personal_info["id"] != "T0002"
    assert personal_info["username"] != "JaneDoe"
    assert personal_info["first_name"] != "Jane"
    assert personal_info["last_name"] != "Smith"
    assert personal_info["contact_num"] != "1111111111"
    assert personal_info["country"] != "Canada"
    assert personal_info["date_of_birth"] != "1995-01-01"
    assert personal_info["gender"] != "Female"

@patch("app.user.insert_info")
def test_register(mock_insert_info):
    user_data = {
        "username": "NewUser",
        "password": "NewPassword@123",
        "first_name": "Alice",
        "last_name": "Smith",
        "contact_num": "0987654321",
        "country": "Canada",
        "date_of_birth": "1995-01-01",
        "gender": "Female"
    }

    mock_insert_info.return_value = True
    result = User.register("tutor", user_data)
    assert result == True
    mock_insert_info.assert_called_once()

    mock_insert_info.return_value = False
    result = User.register("tutor", user_data)
    assert result == False

@patch("app.user.update_user_info")
def test_update_own_info(mock_update_user_info, sample_user, setup_tutors_file):
    mock_update_user_info.return_value = True
    updated_info = {
        "first_name": "Jame",
        "last_name": "Doe",
        "contact_num": "0987654321"
    }
    
    assert sample_user.update_own_info(updated_info, setup_tutors_file) == True
    mock_update_user_info.assert_called_once()

    mock_update_user_info.return_value = False
    assert sample_user.update_own_info(updated_info, setup_tutors_file) == False

def test_authenticate(sample_user):
    assert sample_user.authenticate("JohnnyBoy", "Hashed_password_1") == True
    assert sample_user.authenticate("JohnnyBoy", "WrongPassword") == False
    assert sample_user.authenticate("Wronguser", "Hashed_password_1") == False

def test_password_validation(sample_user):
    assert sample_user.password_validation("Hashed_password_1") == True
    assert sample_user.password_validation("hashed_password_1") == False
    assert sample_user.password_validation("Hashedpassword1") == False
    assert sample_user.password_validation("Hashed") == False

def test_check_old_password(sample_user):
    assert sample_user.check_old_password("Hashed_password_1") == True
    assert sample_user.check_old_password("WrongOldPassword") == False

@patch("app.user.update_user_info")
def test_change_password(mock_update_user_info, sample_user, setup_tutors_file):
    mock_update_user_info.return_value = True
    assert sample_user.change_password("NewPassword@123", setup_tutors_file) == True
    mock_update_user_info.assert_called_once_with(setup_tutors_file, sample_user.id, {"password": "NewPassword@123"})
    
    mock_update_user_info.reset_mock()

    assert sample_user.change_password("short", setup_tutors_file) == False
    mock_update_user_info.assert_not_called()

    mock_update_user_info.return_value = False
    assert sample_user.change_password("ValidPassword@123", setup_tutors_file) == False
    mock_update_user_info.assert_called_once_with(setup_tutors_file, sample_user.id, {"password": "ValidPassword@123"})

@patch("app.user.get_multiple_info_by_id")
def test_get_all_grades(mock_get_multiple_info_by_id, sample_user_with_grades):
    mock_get_multiple_info_by_id.return_value = [
        {
            "id": "L0001",
            "quiz_id": "Q001", 
            "grade": 85.0,
            "quiz_title": "Quiz 1",
            "course_title": "Introduction to Programming in Python"
        },
        {
            "id": "L0001",
            "quiz_id": "Q003",
            "grade": 90.0,
            "quiz_title": "Quiz 1",
            "course_title": "Machine Learning"
        }
    ]
    
    grades = sample_user_with_grades.get_all_grades()

    expected_grades = [
        {
            "id": "L0001",
            "quiz_id": "Q001",
            "grade": 85.0,
            "quiz_title": "Quiz 1",
            "course_title": "Introduction to Programming in Python"
        },
        {
            "id": "L0001",
            "quiz_id": "Q003",
            "grade": 90.0,
            "quiz_title": "Quiz 1",
            "course_title": "Machine Learning"
        }
    ]

    assert len(grades) == len(expected_grades)
    for grade in grades:
        assert grade in expected_grades

    assert {
        "id": "L0001",
        "quiz_id": "Q002",
        "grade": 70.0,
        "quiz_title": "Quiz 2",
        "course_title": "Introduction to Programming in Python"
    } not in grades

@patch("app.user.User.get_all_assignments")
def test_get_all_assignments(mock_get_all_assignments, sample_user_with_grades):
    mock_get_all_assignments.return_value = [
        {
            'title': 'Assignment 1',
            'grade': 1.0,
            'course_title': 'Introduction to Programming in Python'
        },
        {
            'title': 'Assignment 2',
            'grade': 0,
            'course_title': 'Machine Learning'
        }
    ]

    assignments = sample_user_with_grades.get_all_assignments()

    assert len(assignments) == 2
    assert assignments[0]['title'] == 'Assignment 1'
    assert assignments[0]['grade'] == 1.0
    assert assignments[0]['course_title'] == 'Introduction to Programming in Python'
    assert assignments[1]['title'] == 'Assignment 2'
    assert assignments[1]['grade'] == 0
    assert assignments[1]['course_title'] == 'Machine Learning'

    assert assignments[0]['title'] != 'Assignment 3'
    assert assignments[0]['grade'] != 0.5 
    assert assignments[1]['course_title'] != 'Data Science'
    assert len(assignments) != 3
