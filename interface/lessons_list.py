import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os


class LessonsList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master, fg_color="transparent")
        self.lessons_list = course.lessons_list  # Assuming course has a lesson_list attribute
        title_bar = ctk.CTkLabel(self, text=course.title, font=ctk.CTkFont(size=40, weight="bold"))
        title_bar.pack(fill="x", padx=10, pady=10)
        self.lessons_list_frame = ctk.CTkScrollableFrame(self)
        self.lessons_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))  # Added bottom padding
        self.lessons_list_frame.pack_propagate(False)  # Prevent the frame from shrinking
        self.lessons_list_frame.configure(width=800, height=550)  # Reduced height to leave space for back button
        
        self.create_lesson_bars()
        self.hide_page()
        
        self.create_back_button()  # Add back button creation

    def create_lesson_bars(self):
        for lesson in self.lessons_list:
            lesson_frame = ctk.CTkFrame(self.lessons_list_frame)  # Create a frame for each lesson
            lesson_label = ctk.CTkLabel(lesson_frame, text=lesson.title)  # Assuming lesson is a string
            lesson_label.pack(side="left", padx=10, pady=5)
            lesson_frame.pack(fill="x", padx=10, pady=5)  # Pack the lesson frame

            view_button = ctk.CTkButton(lesson_frame, text="View", width=80)
            view_button.pack(side="right", padx=10, pady=5)

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()

    def create_back_button(self):
        back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button_click)
        back_button.pack(side="left", padx=10, pady=10, anchor="sw")  # Sticky to bottom left

    def on_back_button_click(self):
        # Define the action for the back button here
        pass

# if __name__ == "__main__":
#     root = ctk.CTk()
#     lessons_list = LessonsList(root, None, 1)
#     lessons_list.pack(fill="both", expand=True)
#     root.mainloop()
