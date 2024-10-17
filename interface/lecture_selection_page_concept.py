import customtkinter as ctk
from PIL import Image
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.course import Course
from interface.lessons_list import LessonsList
class LectureSelectionPage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header frame
        # Set header frame color to navy
        self.header_frame = ctk.CTkFrame(self, fg_color="#6495ED")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        self.header_frame.grid_columnconfigure(1, weight=1)

        # Logo
        self.logo_image = ctk.CTkImage(Image.open("Picture/EmpowerU Logo.png"), size=(50, 50))
        self.logo_label = ctk.CTkLabel(self.header_frame, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=(10, 20), pady=10)

        # Header text
        self.header_label = ctk.CTkLabel(self.header_frame, text="Dashboard", font=ctk.CTkFont(size=40, weight="bold"))
        self.header_label.grid(row=0, column=1, sticky="w", pady=10)

        # Lectures frame
        self.lectures_frame = ctk.CTkScrollableFrame(self)
        self.lectures_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.lectures_frame.grid_columnconfigure(0, weight=1)

        self.user.course_list = Course.initialize_courses()

        # # Create lecture tiles
        for index, course in enumerate(self.user.course_list):
            lecture_frame = ctk.CTkFrame(self.lectures_frame)
            lecture_frame.grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            lecture_frame.grid_columnconfigure(1, weight=1)

            title_label = ctk.CTkLabel(lecture_frame, text=course.title, font=ctk.CTkFont(size=16, weight="bold"))
            title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

            duration_label = ctk.CTkLabel(lecture_frame, text=course.estimated_duration)
            duration_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 5))

            course_lessons_list = LessonsList(self.master, self.user, course)
            view_button = ctk.CTkButton(lecture_frame, text="View", width=80, command=lambda: self.go_to_lessons_list(course_lessons_list))
            view_button.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky="e")   

        # Back button
        self.back_button = ctk.CTkButton(self, text="Back", width=80, command=self.return_to_dashboard)
        self.back_button.grid(row=2, column=0, padx=10, pady=10, sticky="sw")
    
    def go_to_lessons_list(self, lessons_list):
        self.hide_page()
        lessons_list.show_page()

        # Method to handle back button click
    def return_to_dashboard(self):
        self.hide_page()
        self.user.menu.show_page()

    def show_page(self):
        self.pack(expand=True, fill="both")

    def hide_page(self):
        self.pack_forget()

    
        # Create a main window
# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.title("Lecture Selection")
#     root.geometry("400x300")

#     # Create and pack the LectureSelectionPage
#     lecture_selection_page = LectureSelectionPage(root, None)
#     lecture_selection_page.pack(expand=True, fill="both")

#     # Start the main event loop
#     root.mainloop()

