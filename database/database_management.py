import csv

def extract_info_from_file(file_path):
    print(file_path)
    try:
        with open(file_path, "r", newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []

def get_user_by_id(file_path, id):
    users = extract_info_from_file(file_path)
    for user in users:
        if user.get("ID") == id:
            return user
    return None

def get_tutors():
    file_path = "database/tutors.txt"
    tutors = extract_info_from_file(file_path)
    return tutors

def get_students():
    file_path = "database/learners.txt"
    students = extract_info_from_file(file_path)
    return students

def get_admins():
    file_path = "database/admin.txt"
    admins = extract_info_from_file(file_path)
    return admins

def write_info_to_file(file_path, data):
    try:
        with open(file_path, "w", newline='') as file:
            fieldnames = data[0].keys()
            print(fieldnames)
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def update_user_info(file_path, id, new_info):
    users = extract_info_from_file(file_path)
    updated = False
    for user in users:
        if user.get("ID") == id:
            user.update(new_info)
            updated = True
            break
    
    if updated:
        if write_info_to_file(file_path, users):
            return True
        else:
            print(f"Error: Failed to update user information in file: {file_path}")
    else:
        print(f"Error: User with ID {id} not found in file: {file_path}")
    return False

def add_new_user(role, user_data):
    if role == "learner":
        file_path = "database/learners.txt"
    elif role == "tutor":
        file_path = "database/tutors.txt"
    elif role == "admin":
        file_path = "database/admin.txt"
    
    users = extract_info_from_file(file_path)
    users.append(user_data)
    if write_info_to_file(file_path, users):
        return True
    else:
        print(f"Error: Failed to add new user to file: {file_path}")
    return False
# print(get_admins())
# print(get_students())
# print(get_tutors())

