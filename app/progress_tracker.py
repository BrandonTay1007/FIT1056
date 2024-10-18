class ProgressTracker:
    def __init__(self, learner, courses):
        self.learner = learner
        self.courses = courses
        self.learner.course_progress = {}
        
    def init_progress(self):
        # Initialize progress for all courses
        for course in self.courses:
            self.learner.course_progress[course.id] = {
                'completed_lessons': 0,
                'total_lessons': len(course.lessons_list),
                'progress_percentage': 0
            }
        self.refresh_progress()
    
    def get_course_progress(self, course_id):
        return self.learner.course_progress.get(course_id, None)
    
    def refresh_progress(self):
        for course in self.learner.course_list:
            completed_lessons = sum(1 for lesson in course.lessons_list if lesson.id in self.learner.attempted_lessons)
            self.learner.course_progress[course.id]['completed_lessons'] = completed_lessons
            self.update_progress(course.id)

    def update_progress(self, course_id):
        completed_lessons = self.learner.course_progress[course_id]['completed_lessons']
        total_lessons = self.learner.course_progress[course_id]['total_lessons']
        self.learner.course_progress[course_id]['progress_percentage'] = round(
            (completed_lessons / total_lessons) * 100, 2
        )
    
    def get_overall_progress(self):
        if not self.learner.course_progress:
            return 0
        
        total_progress = sum(course['progress_percentage'] for course in self.learner.course_progress.values())
        return round(total_progress / len(self.learner.course_progress), 2)
