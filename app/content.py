class Content:
    def __init__(self, id, title, type, content):
        self.id = id
        self.title = title
        self.type = type
        self.content = content

    def get_content(self):
        return (self.type, self.content)

    
    
