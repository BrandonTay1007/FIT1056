import customtkinter as ctk
from app import *
class EditLessonsListPage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.user.course_list = Course.initialize_courses(self.user)
        for course in self.user.course_list:
            self.lessons_by_course[course.title] = Lessons.list_lessons_by_course(course.id)
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Edit Lessons", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=580)
        self.scrollable_frame.pack(padx=10, pady=10, expand=True, fill="both")

        self.display_lessons()

        self.add_lesson_button = ctk.CTkButton(self, text="Add New Lesson", command=self.add_new_lesson)
        self.add_lesson_button.pack(pady=10)

    def display_lessons(self):
        for course_name, lessons in self.lessons_by_course.items():
            course_frame = ctk.CTkFrame(self.scrollable_frame)
            course_frame.pack(padx=10, pady=(20, 10), fill="x", expand=True)

            course_label = ctk.CTkLabel(course_frame, text=course_name, font=("Arial", 18, "bold"))
            course_label.pack(anchor="w", padx=10, pady=5)

            for lesson in lessons:
                lesson_frame = ctk.CTkFrame(course_frame)
                lesson_frame.pack(padx=20, pady=5, fill="x")

                lesson_label = ctk.CTkLabel(lesson_frame, text=f"{lesson['title']} (Type: {lesson['lesson_type']})")
                lesson_label.pack(side="left", padx=10, pady=5)

                edit_button = ctk.CTkButton(lesson_frame, text="Edit", width=60, 
                                            command=lambda l=lesson: self.edit_lesson(l))
                edit_button.pack(side="right", padx=(0, 10), pady=5)

                delete_button = ctk.CTkButton(lesson_frame, text="Delete", width=60, fg_color="red", hover_color="dark red",
                                              command=lambda l=lesson: self.delete_lesson(l))
                delete_button.pack(side="right", padx=10, pady=5)

    def edit_lesson(self, lesson):
        edit_window = ctk.CTkToplevel(self)
        edit_window.title(f"Edit Lesson: {lesson['title']}")
        edit_window.geometry("400x300")

        title_label = ctk.CTkLabel(edit_window, text="Title:")
        title_label.pack(pady=(20, 5))
        title_entry = ctk.CTkEntry(edit_window, width=300)
        title_entry.insert(0, lesson['title'])
        title_entry.pack()

        type_label = ctk.CTkLabel(edit_window, text="Type:")
        type_label.pack(pady=(20, 5))
        type_entry = ctk.CTkEntry(edit_window, width=300)
        type_entry.insert(0, lesson['lesson_type'])
        type_entry.pack()

        save_button = ctk.CTkButton(edit_window, text="Save Changes", 
                                    command=lambda: self.save_lesson_changes(lesson['id'], title_entry.get(), type_entry.get(), edit_window))
        save_button.pack(pady=20)

    def save_lesson_changes(self, lesson_id, new_title, new_type, window):
        Lessons.update_lesson(lesson_id, {'title': new_title, 'lesson_type': new_type})
        self.refresh_lessons()
        window.destroy()

    def delete_lesson(self, lesson):
        if ctk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the lesson '{lesson['title']}'?"):
            Lessons.delete_lesson(lesson['id'])
            self.refresh_lessons()

    def add_new_lesson(self):
        add_window = ctk.CTkToplevel(self)
        add_window.title("Add New Lesson")
        add_window.geometry("400x350")

        title_label = ctk.CTkLabel(add_window, text="Title:")
        title_label.pack(pady=(20, 5))
        title_entry = ctk.CTkEntry(add_window, width=300)
        title_entry.pack()

        type_label = ctk.CTkLabel(add_window, text="Type:")
        type_label.pack(pady=(20, 5))
        type_entry = ctk.CTkEntry(add_window, width=300)
        type_entry.pack()

        course_label = ctk.CTkLabel(add_window, text="Course:")
        course_label.pack(pady=(20, 5))
        course_dropdown = ctk.CTkOptionMenu(add_window, values=list(self.lessons_by_course.keys()))
        course_dropdown.pack()

        save_button = ctk.CTkButton(add_window, text="Add Lesson", 
                                    command=lambda: self.save_new_lesson(title_entry.get(), type_entry.get(), course_dropdown.get(), add_window))
        save_button.pack(pady=20)

    def save_new_lesson(self, title, lesson_type, course_name, window):
        course_id = Lessons.get_course_id_by_name(course_name)
        if course_id is None:
            ctk.messagebox.showerror("Error", f"Course '{course_name}' not found.")
            return

        new_lesson = {
            'id': str(len(self.lessons_by_course[course_name]) + 1),  # Simple ID generation, you might want to improve this
            'title': title,
            'lesson_type': lesson_type,
            'course_id': course_id
        }
        Lessons.add_new_lesson(new_lesson)
        self.refresh_lessons()
        window.destroy()

    def refresh_lessons(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.display_lessons()

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
