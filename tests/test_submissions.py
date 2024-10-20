import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import patch, MagicMock
from app.submissions import Submission
from database.database_management import *
from app.empoweru_constants import *
from datetime import datetime

mock_user_data = {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe"
}

mock_assignment_data = {
    "id": 1,
    "title": "Assignment 1"
}

@pytest.fixture
def submission():
    return Submission(
        assignment_id=1,
        user_id=1,
        file_path="c:\\Users\\taywe\\Monash\\FIT1056\\deliverable2\\database\\submissions\\Marking Rubric Deliverable 2 (1).pdf",
        submission_date="2024-10-19T12:21",
        graded=True,
        grade=1.0,
        feedback=""
    )

def test_get_user_name(submission):
    with patch('app.submissions.get_info_by_id', return_value=mock_user_data):
        assert submission.get_username() == "John Doe"

    with patch('app.submissions.get_info_by_id', return_value=None):
        assert submission.get_username() == "Unknown User"

def test_grade_submission(submission):
    with patch('app.submissions.relational_id_update', return_value=True):
        submission.feedback = "Well done!"
        submission.grade = 95
        success = submission.grade_submission()
        assert success is True

    with patch('app.submissions.relational_id_update', return_value=False):
        submission.feedback = "Needs more work."
        submission.grade = 50
        success = submission.grade_submission()
        assert success is False

def test_get_assignment_title(submission):
    with patch('app.submissions.get_info_by_id', return_value=mock_assignment_data):
        assert submission.get_assignment_title() == "Assignment 1"

def test_get_submission_date(submission):
    assert submission.get_submission_date() == datetime(2024, 10, 19, 12, 21)

def test_get_file_path(submission):
    assert submission.get_file_path() == "c:\\Users\\taywe\\Monash\\FIT1056\\deliverable2\\database\\submissions\\Marking Rubric Deliverable 2 (1).pdf"