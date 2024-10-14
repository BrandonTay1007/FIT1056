from database.database_management import *
from empoweru_constants import *

class Course:
    def __init__(self, id, title, estimated_duration, lessons_list):
        self.id = id
        self.title = title
        self.estimated_duration = estimated_duration
        self.lessons_list = lessons_list
        
    
    def __str__(self):
        return f"Course: {self.title}"
    
    def initialize_courses():
        available_courses = extract_file_info(COURSES_FILE_PATH)
        return available_courses
            
    