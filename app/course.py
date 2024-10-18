import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.lessons import Lessons
from database.database_management import *
from empoweru_constants import *
from app.quiz import Quiz

class Course:
    def __init__(self, id, title, estimated_duration, description, lessons_id_list):
        self.id = id
        self.title = title
        self.estimated_duration = estimated_duration
        self.description = description
        self.lessons_list = []
        self.progress = 0
        self.quizzes = Quiz.init_by_course_id(self.id)
        if len(self.lessons_list) == 0:
            for id in lessons_id_list:
                lesson = get_info_by_id(LESSONS_FILE_PATH, "id", id)
                if lesson is not None:
                    self.lessons_list.append(Lessons(lesson["id"], lesson["title"], lesson["type"], lesson["content_list"]))
                else:
                    print(f"\033[1;31mLesson with id {id} not found\033[0m")

    def __str__(self):
        return f"Course: {self.title}"
    
    def add_course(id, title, estimated_duration, description, lessons_id_list):
        course = Course(id, title, estimated_duration, description, lessons_id_list)
        insert_info(COURSES_FILE_PATH, course)
        return course

    def initialize_courses():
        available_courses = []

        for course in extract_file_info(COURSES_FILE_PATH):
            available_courses.append(Course(course["id"], course["title"], course["estimated_duration"], course["description"], course["lessons_id_list"]))

        return available_courses
