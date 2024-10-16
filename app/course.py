import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from empoweru_constants import *

class Course:
    def __init__(self, id, title, estimated_duration, description, lessons_id_list):
        self.id = id
        self.title = title
        self.estimated_duration = estimated_duration
        self.description = description
        self.lessons_id_list = lessons_id_list
        
    
    def __str__(self):
        return f"Course: {self.title}"
    
    def initialize_courses():
        available_courses = []

        for course in extract_file_info(COURSES_FILE_PATH):
            available_courses.append(Course(course["id"], course["title"], course["estimated_duration"], course["description"], course["lessons_id_list"]))

        return available_courses
     
if __name__ == "__main__":
    for i in Course.initialize_courses():
        print(i)
