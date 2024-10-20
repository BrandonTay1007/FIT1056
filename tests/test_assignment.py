import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from app.assignment import Assignment  

import pytest
from datetime import datetime


@pytest.fixture
def sample_assignment_data():
    return {
        'id': 1,
        'title': 'Test Assignment',
        'due_date': datetime(2024, 10, 20),
        'pdf_path': '/path/to/pdf',
        'associated_course_id': 101
    }

@pytest.fixture
def sample_assignment(sample_assignment_data):
    return Assignment(
        sample_assignment_data['id'],
        sample_assignment_data['title'],
        sample_assignment_data['due_date'],
        sample_assignment_data['pdf_path'],
        sample_assignment_data['associated_course_id']
    )


# Test submission handling
def test_submission(sample_assignment):
    assert sample_assignment.is_submitted() is False
    sample_assignment.set_submission('My submission')
    assert sample_assignment.get_submission() == 'My submission'
    assert sample_assignment.is_submitted() is True


# Test submission overdue functionality
def test_is_overdue(sample_assignment):
    future_date = datetime(2024, 10, 21)
    past_date = datetime(2024, 10, 19)
    assert sample_assignment.is_overdue(future_date) is True
    assert sample_assignment.is_overdue(past_date) is False