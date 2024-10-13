class Course:
    def __init__(self, id, title, description, estimated_duration):
        self.id = id
        self.title = title
        self.description = description
        self.estimated_duration = estimated_duration
        self.course_content = []
        

    def __str__(self):
        return f"Course: {self.title}"
    