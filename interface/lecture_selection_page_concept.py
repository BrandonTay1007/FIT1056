import customtkinter as ctk
from PIL import Image
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from interface.lessons_list import LessonsList
from app.learners import Learner
from interface.progress_bar import ProgressBar
from app.progress_tracker import ProgressTracker

class LectureSelectionPage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color='transparent')
        self.user = user
        self.user.lecture_selection_page = self
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header frame
        # Set header frame color to navy
        self.header_frame = ctk.CTkFrame(self, fg_color="#6495ED")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=0)

        # Logo
        self.logo_image = ctk.CTkImage(Image.open("Picture/EmpowerU Logo.png"), size=(50, 50))
        self.logo_label = ctk.CTkLabel(self.header_frame, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=(10, 20), pady=10)

        # Header text
        self.header_label = ctk.CTkLabel(self.header_frame, text="Dashboard", font=ctk.CTkFont(size=40, weight="bold"))
        self.header_label.grid(row=0, column=1, sticky="w", pady=10)

        # Lectures frame
        self.lectures_frame = ctk.CTkScrollableFrame(self, fg_color='transparent')
        self.lectures_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.lectures_frame.grid_columnconfigure(0, weight=1)


        # Initialize ProgressTracker
        self.progress_tracker = ProgressTracker(self.user, self.user.course_list)
        self.progress_tracker.init_progress()
        
        self.create_lecture_tiles()

        # Add back button at bottom left corner
        self.back_button = ctk.CTkButton(self, text="Back", command=self.return_to_dashboard, bg_color="transparent")
        self.back_button.grid(row=2, column=0, padx=10, pady=10, sticky="sw")

    def create_lecture_tiles(self):
        for widget in self.lectures_frame.winfo_children():
            widget.destroy()

        for index, course in enumerate(self.user.course_list):
            lecture_frame = ctk.CTkFrame(self.lectures_frame)
            lecture_frame.grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            lecture_frame.grid_columnconfigure(1, weight=1)

            title_label = ctk.CTkLabel(lecture_frame, text=course.title, font=ctk.CTkFont(size=16, weight="bold"))
            title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

            duration_label = ctk.CTkLabel(lecture_frame, text=course.estimated_duration)
            duration_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 5))

            progress_percentage = ctk.CTkLabel(lecture_frame, text="0%", width=40)
            progress_percentage.grid(row=2, column=0, padx=(10, 0), pady=(0, 5), sticky="w")

            progress_bar = ProgressBar(lecture_frame, width=100)
            progress_bar.grid(row=2, column=0, padx=(60, 10), pady=(0, 5), sticky="w")
            
            course_progress = self.progress_tracker.get_course_progress(course.id)
            if course_progress:
                progress_percentage_value = course_progress['progress_percentage']
                progress_bar.update_progress(progress_percentage_value / 100)
                progress_percentage.configure(text=f"{progress_percentage_value:.0f}%")

            course_lessons_list = LessonsList(self.master, self.user, course)
            view_button = ctk.CTkButton(
                lecture_frame,
                text="View",
                width=80,
                command=lambda cl=course_lessons_list: self.go_to_lessons_list(cl)
            )
            view_button.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky="e")

    def refresh_progress_bars(self):
        self.progress_tracker.refresh_progress()
        self.create_lecture_tiles()

    def go_to_lessons_list(self, lessons_list):
        self.hide_page()
        lessons_list.show_page()

    def return_to_dashboard(self):
        self.hide_page()
        self.user.menu.show_page()

    def show_page(self):
        self.pack(expand=True, fill="both")
        self.refresh_progress_bars()  # Add this line to refresh when showing the page

    def hide_page(self):
        self.pack_forget()

    
# Create a main window
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Lecture Selection")
    root.geometry("1400x700")

    # Create and pack the LectureSelectionPage
    # Create a learner with the provided information
    user = Learner(
        id="L001",
        username="johndoe",
        password="hashed_password_1",
        first_name="John",
        last_name="Doe",
        contact_num="+1234567890",
        country="United States",
        date_of_birth="1998-05-15",
        gender="Male",
        profile_picture_path="/profiles/johndoe.jpg",
        attempted_lessons=[1,2],
        attempted_quizzes=[1,2]
    )
    lecture_selection_page = LectureSelectionPage(root, user)
    lecture_selection_page.pack(expand=True, fill="both")

    # Start the main event loop
    root.mainloop()
