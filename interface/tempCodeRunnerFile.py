
# from app.content import Content
# from database.database_management import get_info_by_id
# from app.lessons import Lessons

# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.geometry("1200x800")
#     lesson_info = get_info_by_id(LESSONS_FILE_PATH, 1)
#     lesson_content_list = []
#     for content in lesson_info["content_list"]:
#         print(content)
#         lesson_content_list.append(Content(content["id"], content["title"], content["type"], content["content"]))

#     l = Lessons(1, lesson_info["title"], lesson_info["type"], lesson_content_list)
#     page = LessonsPage(root, l)
#     page.pack(fill="both", expand=True)
#     root.mainloop()
