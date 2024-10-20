import json
import os
import shutil
from app.empoweru_constants import BASE_DIR

def extract_file_info(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: File is not a valid JSON: {file_path}")
        return []

def get_multiple_info_by_id(file_path, key, id):
    all_data = extract_file_info(file_path)
    return [data for data in all_data if data.get(key) == id]

def get_info_by_id(file_path, key, id):
    all_data = extract_file_info(file_path)
    for data in all_data:
        if data.get(key) == id:
            print(f"\033[1;32mData of id {id} in {file_path} obtained successfully\033[0m")
            return data
    print(f"\033[1;31mData not found: {id} in {file_path}\033[0m")
    return None

def write_info_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def relational_id_update(file_path, first_id, first_key, second_id, second_key, new_info):
    all_data = extract_file_info(file_path)
    updated = False
    for data in all_data:
        if data.get(first_key) == first_id and data.get(second_key) == second_id:
            data.update(new_info)
            updated = True
            break
    
    if not updated:
        all_data.append(new_info)
        updated = True

    if updated:
        if write_info_to_file(file_path, all_data):
            print(f"\033[1;32mData updated successfully in {file_path}\033[0m")
            return True
        else:
            print(f"\033[1;31mError: Failed to update user information in file: {file_path}\033[0m")
    else:
        print(f"\033[1;31mError: User with ID {id} not found in file: {file_path}\033[0m")
    return False

def update_info_by_id(file_path, key, id, new_info):
    all_data = extract_file_info(file_path)
    updated = False
    for data in all_data:
        if data.get(key) == id:
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

def remove_by_id(file_path, id):
    all_data = extract_file_info(file_path)
    updated = False
    for data in all_data:
        if data.get("id") == id:
            all_data.remove(data)
            updated = True
            break
    
    if updated:
        if write_info_to_file(file_path, all_data):
            print(f"\033[1;32mData deleted successfully from {file_path}\033[0m")
            return True
        else:
            print(f"Error: Failed to delete user information in file: {file_path}")
    else:
        print(f"Error: User with ID {id} not found in file: {file_path}")
    return False
    
    
def insert_info(file_path, data):
    all_data = extract_file_info(file_path)
    all_data.append(data)
    if write_info_to_file(file_path, all_data):
        print(f"\033[1;32mData added to file: {file_path}\033[0m")
        return True
    else:
        print(f"\033[1;31mError: Failed to add data to file: {file_path}\033[0m")
    return False

def get_absolute_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)

def read_file_content(relative_path):
    try:
        with open(get_absolute_path(relative_path), 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {relative_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def get_file_name(relative_path):
    return os.path.basename(relative_path)

def copy_file(source_path, destination_folder):
    abs_destination_folder = get_absolute_path(destination_folder)
    os.makedirs(abs_destination_folder, exist_ok=True)
    new_file_path = os.path.join(abs_destination_folder, os.path.basename(source_path))
    try:
        shutil.copy2(source_path, new_file_path)
        return os.path.relpath(new_file_path, BASE_DIR)
    except Exception as e:
        print(f"Error copying file: {str(e)}")
        return None

def write_file_content(relative_path, content):
    try:
        with open(get_absolute_path(relative_path), 'wb') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing file: {str(e)}")
        return False

# def main():
#     print(update_user_info("database/admin.json", "A0001", {"username": "CHANGED"}))
# for i in extract_file_info("database/lessons.json"):
#     print(i)
