import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from unittest.mock import patch, MagicMock
from app.user import User
from app.admin import Admin
from app.empoweru_constants import ADMIN_FILE_PATH, TUTORS_FILE_PATH, LEARNERS_FILE_PATH
 
@pytest.fixture
def admin():
    return Admin(
        id='A0001',
        username='admin_user',
        password='password',
        first_name='Admin',
        last_name='User',
        contact_num='1234567890',
        country='Country',
        date_of_birth='2000-01-01',
        gender='M'
    )

def test_register():
    user_data = {'username': 'new_user', 'password': 'new_password', 'first_name': 'New', 'last_name': 'User'}
    
    with patch.object(User, 'register', return_value=True) as mock_register:
        result = Admin.register(user_data)
        mock_register.assert_called_once_with(user_data, "admin")
        assert result is True

    with patch.object(User, 'register', return_value=False) as mock_register:
        result = Admin.register(user_data)
        mock_register.assert_called_once_with(user_data, "admin")
        assert result is False

def test_register_new_user(admin):
    role = "learner"
    user_data = {
        'username': 'learner_user', 
        'password': 'learner_password', 
        'first_name': 'Learner', 
        'last_name': 'User'
    }
    
    with patch.object(User, 'register', return_value=True) as mock_register:
        result = admin.register_new_user(role, user_data)
        mock_register.assert_called_once_with(role, user_data)
        assert result is True

    with patch.object(User, 'register', return_value=False) as mock_register:
        result = admin.register_new_user(role, user_data)
        mock_register.assert_called_once_with(role, user_data)
        assert result is False
    
def test_get_users_info(admin):
    user_id = 1
    role = "tutors"
    
    with patch('app.admin.get_info_by_id', return_value={'id': user_id, 'name': 'Tutor User'}) as mock_get_info:
        result = admin.get_users_info(user_id, role)
        mock_get_info.assert_called_once_with(admin.get_user_file_path(role), "id", user_id)
        assert result == {'id': user_id, 'name': 'Tutor User'}

    with patch('app.admin.get_info_by_id', return_value=None) as mock_get_info:
        result = admin.get_users_info(user_id, role)
        mock_get_info.assert_called_once_with(admin.get_user_file_path(role), "id", user_id)
        assert result is None

def test_get_user_file_path(admin):
    assert admin.get_user_file_path("admin") == ADMIN_FILE_PATH
    assert admin.get_user_file_path("tutors") == TUTORS_FILE_PATH
    assert admin.get_user_file_path("learners") == LEARNERS_FILE_PATH
    assert admin.get_user_file_path("invalid_role") is None

def test_change_user_info(admin):
    role = "learners"
    user_id = 1
    new_info = {'username': 'updated_user'}
    
    with patch('app.admin.update_user_info', return_value=True) as mock_update:
        result = admin.change_user_info(role, user_id, new_info)
        mock_update.assert_called_once_with(admin.get_user_file_path(role), user_id, new_info)
        assert result is True

    with patch('app.admin.update_user_info', return_value=False) as mock_update:
        result = admin.change_user_info(role, user_id, new_info)
        mock_update.assert_called_once_with(admin.get_user_file_path(role), user_id, new_info)
        assert result is False

def test_delete_user(admin):
    user_id = 1
    role = "learners"
    
    with patch('app.admin.remove_by_id', return_value=True) as mock_remove:
        result = admin.delete_user(user_id, role)
        mock_remove.assert_called_once_with(admin.get_user_file_path(role), user_id)
        assert result is True
    
    with patch('app.admin.remove_by_id', return_value=False) as mock_remove:
        result = admin.delete_user(user_id, role)
        mock_remove.assert_called_once_with(admin.get_user_file_path(role), user_id)
        assert result is False

def test_update_own_info(admin):
    updated_info = {'username': 'new_admin_user'}
    
    with patch.object(User, 'update_own_info', return_value=True) as mock_update:
        result = admin.update_own_info(updated_info)
        mock_update.assert_called_once_with(admin, updated_info, ADMIN_FILE_PATH)
        assert result is True

    with patch.object(User, 'update_own_info', return_value=False) as mock_update:
        result = admin.update_own_info(updated_info)
        mock_update.assert_called_once_with(admin, updated_info, ADMIN_FILE_PATH)
        assert result is False

def test_change_password(admin):
    new_password = 'new_secure_password'
    
    with patch.object(User, 'change_password', return_value=True) as mock_change_password:
        result = admin.change_password(new_password)
        mock_change_password.assert_called_once_with(admin, new_password, ADMIN_FILE_PATH)
        assert result is True

    with patch.object(User, 'change_password', return_value=False) as mock_change_password:
        result = admin.change_password(new_password)
        mock_change_password.assert_called_once_with(admin, new_password, ADMIN_FILE_PATH)
        assert result is False
