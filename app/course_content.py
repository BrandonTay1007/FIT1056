class CourseContent:
    def __init__(self):
        self.content = []

    def add_sub_header(self, title):
        self.content.append({
            'type': 'sub_header',
            'title': title,
            'items': []
        })

    def create_lesson(self, title, icon_type, is_completed=False, parent_index=-1):
        lesson = {
            'type': 'lesson',
            'title': title,
            'icon_type': icon_type,
            'is_completed': is_completed
        }
        
        if parent_index >= 0 and parent_index < len(self.content):
            self.content[parent_index]['items'].append(lesson)
        else:
            self.content.append(lesson)
    def get_lessons_list(self):
        lessons_list = []
        for item in self.content:
            if item['type'] == 'lesson':
                lessons_list.append(item)
        return lessons_list

    def get_content(self):
        return self.content
