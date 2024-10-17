import customtkinter as ctk

# Font constants
TITLE_FONT = ("Roboto", 20)
TYPE_FONT = ("Roboto", 12, "bold")
TEXT_FONT = ("Roboto", 14)

class GradePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        # Create a main frame to hold both the scrollable frame and the back button
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill=ctk.BOTH, expand=True)
        
        # Move the scrollable frame inside the main frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        self.scrollable_frame.pack(fill=ctk.BOTH, expand=True, padx=20)

        self.title_label = ctk.CTkLabel(self.scrollable_frame, text="Grades", font=TITLE_FONT)
        self.title_label.pack(pady=20)

        assignment_frame = self.add_grades("ASSIGNMENT", "Assignment 3 \"A3\" (in teams)", "10/10")
        quiz_frame = self.add_grades("QUIZ", "In-class test 1 \"T1\"", "10/15")
        assignment_frame = self.add_grades("ASSIGNMENT", "Assignment 3 \"A3\" (in teams)", "10/10")
        quiz_frame = self.add_grades("QUIZ", "In-class test 1 \"T1\"", "10/15")
        assignment_frame = self.add_grades("ASSIGNMENT", "Assignment 3 \"A3\" (in teams)", "10/10")
        quiz_frame = self.add_grades("QUIZ", "In-class test 1 \"T1\"", "10/15")
        assignment_frame = self.add_grades("ASSIGNMENT", "Assignment 3 \"A3\" (in teams)", "10/10")
        quiz_frame = self.add_grades("QUIZ", "In-class test 1 \"T1\"", "10/15")
        assignment_frame = self.add_grades("ASSIGNMENT", "Assignment 3 \"A3\" (in teams)", "10/10")
        quiz_frame = self.add_grades("QUIZ", "In-class test 1 \"T1\"", "10/15")

        # Move the back button outside the scrollable frame
        self.back_button = ctk.CTkButton(self.main_frame, text="Back", command=self.hide_grade_page)
        self.back_button.pack(pady=10, padx=20, anchor="w")


    def add_grades(self, assignment_type, name, grade):
        grade_frame = ctk.CTkFrame(self.scrollable_frame)
        grade_frame.pack(padx=20, pady=10, fill=ctk.BOTH, expand=True)

        type_label = ctk.CTkLabel(grade_frame, text=assignment_type, font=TYPE_FONT)
        type_label.pack(anchor="w")

        info_frame = ctk.CTkFrame(grade_frame, fg_color="transparent")
        info_frame.pack(fill=ctk.X, expand=True)

        name_label = ctk.CTkLabel(info_frame, text=f"{name}", font=TEXT_FONT)
        name_label.pack(side="left", anchor="w")

        grade_label = ctk.CTkLabel(info_frame, text=f"{grade}", font=TEXT_FONT)
        grade_label.pack(side="right", padx=(0, 10))

        review_button = ctk.CTkButton(grade_frame, text="Review", command=None)
        review_button.pack(side="right", padx=(0, 10))

        return grade_frame

    def show_page(self):
        self.main_frame.pack_forget()

    def hide_page(self):
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def go_back(self):
        # This method will be called when the back button is clicked
        # You'll need to implement the logic to return to the previous page
        pass
