import customtkinter as ctk

# Font constants
TITLE_FONT = ("Roboto", 20)
TYPE_FONT = ("Roboto", 12, "bold")
TEXT_FONT = ("Roboto", 14)

class GradePage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        self.user = user
        
        self.title_label = ctk.CTkLabel(self, text="Your Grades", font=TITLE_FONT)
        self.title_label.pack(pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable_frame.pack(fill=ctk.BOTH, expand=True, padx=20)

        self.load_grades()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back_to_menu)
        self.back_button.pack(pady=10, padx=20, anchor="w")

    def update_grades(self):
        self.user.get_all_grades()
        # Remove old widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.load_grades()

    def load_grades(self):
        grades = self.user.get_all_grades()
        
        # Group grades by course
        courses = {}
        for grade_data in grades:
            course = grade_data['course_title']
            if course not in courses:
                courses[course] = []
            courses[course].append(grade_data)
        
        # Display grades for each course
        for course, course_grades in courses.items():
            self.add_course_section(course, course_grades)

    def add_course_section(self, course_name, course_grades):
        course_frame = ctk.CTkFrame(self.scrollable_frame)
        course_frame.pack(padx=20, pady=(20, 10), fill=ctk.X)

        course_label = ctk.CTkLabel(course_frame, text=course_name, font=TYPE_FONT)
        course_label.pack(anchor="w", padx=10, pady=5)

        for grade_data in course_grades:
            self.add_grade(course_frame, grade_data['quiz_title'], f"{grade_data['grade']:.2f}%")

    def add_grade(self, parent_frame, quiz_name, grade):
        grade_frame = ctk.CTkFrame(parent_frame)
        grade_frame.pack(padx=10, pady=5, fill=ctk.X)

        name_label = ctk.CTkLabel(grade_frame, text=quiz_name, font=TEXT_FONT)
        name_label.pack(side="left", anchor="w")

        grade_label = ctk.CTkLabel(grade_frame, text=grade, font=TEXT_FONT)
        grade_label.pack(side="right", padx=(0, 10))

    def back_to_menu(self):
        self.hide_grade_page()
        self.user.menu.show_page()

    def show_page(self):
        self.pack(expand=True, fill="both")

    def hide_grade_page(self):
        self.pack_forget()
