import json

def extract_file_info(file_path):
    print(file_path)
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: File is not a valid JSON: {file_path}")
        return []

def get_info_by_id(file_path, id):
    all_data = extract_file_info(file_path)
    for data in all_data:
        if data.get("id") == id:
            return data
    return None

def write_info_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def update_user_info(file_path, id, new_info):
    all_data = extract_file_info(file_path)
    updated = False
    for data in all_data:
        if data.get("id") == id:
            data.update(new_info)
            updated = True
            break
    
    if updated:
        if write_info_to_file(file_path, all_data):
            return True
        else:
            print(f"Error: Failed to update user information in file: {file_path}")
    else:
        print(f"Error: User with ID {id} not found in file: {file_path}")
    return False

def add_new_user(role, data, file_path):
    if role == "learner":
        file_path = "database/learners.json"
    elif role == "tutor":
        file_path = "database/tutors.json"
    elif role == "admin":
        file_path = "database/admin.json"
    
    all_data = extract_file_info(file_path)
    all_data.append(data)
    if write_info_to_file(file_path, all_data):
        return True
    else:
        print(f"Error: Failed to add data to file: {file_path}")
    return False

# def main():
#     print(update_user_info("database/admin.json", "A0001", {"username": "CHANGED"}))

# main()