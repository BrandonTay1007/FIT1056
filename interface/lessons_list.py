import customtkinter as ctk
from interface.lessons_page import LessonsPage
from interface.quiz_list import QuizList
from interface.assignment_list import AssignmentList

class LessonsList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        # Initialize LessonsList frame
        # Set up user, course, and lessons list
        super().__init__(master)
        self.master = master
        self.user = user    
        self.course = course
        self.lessons_list = course.lessons_list
        
        self.configure(fg_color="#1E1E1E")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create and pack the title bar
        title_bar = ctk.CTkLabel(self, text=self.course.title, font=ctk.CTkFont(size=24, weight="bold"))
        title_bar.pack(fill="x", padx=10, pady=10)
        
        # Create and pack the scrollable frame for lessons
        self.lessons_list_frame = ctk.CTkScrollableFrame(self)
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        # Create lesson bars, back button, and navigation buttons
        self.create_lesson_bars()
        self.create_back_button()
        self.create_navigation_buttons()
        
    def create_lesson_bars(self):
        # Create individual lesson bars for each lesson in the course
        # Display a message if no lessons are available
        if not self.lessons_list:
            no_lessons_label = ctk.CTkLabel(self.lessons_list_frame, text="No lessons available", fg_color="#3B3B3B")
            no_lessons_label.pack(pady=20, fill="x")
            print("No lessons available")
            return

        # Create a frame for each lesson with a view button
        for index, lesson in enumerate(self.lessons_list):
            lesson_frame = ctk.CTkFrame(self.lessons_list_frame, fg_color="#3B3B3B")
            lesson_frame.pack(fill="x", padx=10, pady=5)

            lesson_label = ctk.CTkLabel(lesson_frame, text=f"{index + 1}. {lesson.title}", anchor="w", fg_color="#3B3B3B")
            lesson_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            view_button = ctk.CTkButton(lesson_frame, text="View", width=80)
            view_button.pack(side="right", padx=10, pady=5)
            view_button.configure(command=lambda lesson=lesson: self.view_content(lesson))
            
    def view_content(self, lesson):
        # Handle viewing a specific lesson's content
        # Hide current page, create lesson page, and update user progress
        self.hide_page()
        self.create_lesson_page(lesson)
        if lesson.id not in self.user.attempted_lessons:
            self.user.update_progress(lessons_id=lesson.id)
        
    def create_lesson_page(self, lesson):
        # Create and display the page for a specific lesson
        # Create and show the lesson page
        self.lessons_page = LessonsPage(self.master, lesson, self.user)
        self.master.lessons_list = self
        self.lessons_page.show_page()

    def create_back_button(self):
        # Create a back button to return to the previous page
        # Create and pack the back button
        self.back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button_click)
        self.back_button.pack(side="bottom", padx=10, pady=10, anchor="sw")

    def on_back_button_click(self):
        # Handle the back button click event
        # Handle back button click: hide current page and show lecture selection page
        self.hide_page()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()
        self.user.lecture_selection_page.show_page()
        self.user.lecture_selection_page.progress_tracker.init_progress()
    
    def show_page(self):
        # Display the lessons list page
        # Show the lessons list page
        self.pack(fill="both", expand=True)
        self.show_back_button()

    def hide_page(self):
        # Hide the lessons list page
        # Hide the lessons list page and lesson page if it exists
        self.pack_forget()
        if hasattr(self, 'lessons_page'):
            self.lessons_page.hide_page()

    def create_navigation_buttons(self):
        # Create navigation buttons for lessons, quizzes, and assignments
        # Create and pack navigation buttons for lessons, quizzes, and assignments
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.lessons_button = ctk.CTkButton(self.button_frame, text="Lessons", command=self.show_lessons)
        self.lessons_button.pack(side="left", padx=(0, 5))
        
        self.quizzes_button = ctk.CTkButton(self.button_frame, text="Quizzes", command=self.show_quizzes)
        self.quizzes_button.pack(side="left", padx=(5, 0))
        
        self.assignments_button = ctk.CTkButton(self.button_frame, text="Assignments", command=self.show_assignments)
        self.assignments_button.pack(side="left", padx=(5, 0))

    def show_lessons(self):
        # Display the lessons section
        # Show lessons list and hide quizzes and assignments
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        if hasattr(self, 'quiz_list'):
            self.quiz_list.pack_forget()
        if hasattr(self, 'assignment_list'):
            self.assignment_list.hide_page()
        self.show_back_button()
        
    def show_quizzes(self):
        # Display the quizzes section
        # Show quizzes and hide lessons and assignments
        self.lessons_list_frame.pack_forget()
        if hasattr(self, 'assignment_list'):
            self.assignment_list.hide_page()
        if not hasattr(self, 'quiz_list'):
            self.quiz_list = QuizList(self, self.user, self.course)
        self.quiz_list.pack(fill="both", expand=True)

    def show_assignments(self):
        # Display the assignments section
        # Show assignments and hide lessons and quizzes
        self.lessons_list_frame.pack_forget()
        if hasattr(self, 'quiz_list'):
            self.quiz_list.pack_forget()
        if not hasattr(self, 'assignment_list'):
            self.assignment_list = AssignmentList(self, self.user, self.course)
        self.assignment_list.show_page()

    def hide_navigation_buttons(self):
        # Hide the navigation buttons
        # Hide the navigation buttons
        self.button_frame.pack_forget()

    def show_navigation_buttons(self):
        # Show the navigation buttons
        # Show the navigation buttons
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    def hide_back_button(self):
        # Hide the back button
        # Hide the back button
        self.back_button.pack_forget()

    def show_back_button(self):
        # Show the back button
        # Show the back button
        self.back_button.pack(side="bottom", padx=10, pady=10, anchor="sw")
# if __name__ == "__main__":
#     root = ctk.CTk()
#     lessons_list = LessonsList(root, None, 1)
#     lessons_list.pack(fill="both", expand=True)
#     root.mainloop()

