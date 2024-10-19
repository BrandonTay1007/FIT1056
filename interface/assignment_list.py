import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.assignment_page import AssignmentPage

class AssignmentList(ctk.CTkFrame):
    def __init__(self, master, user, course):
        super().__init__(master)
        self.master = master
        self.user = user
        self.course = course
        self.assignments = course.assignments
        self.configure(fg_color="#1E1E1E")
        self.create_widgets()
        
    def create_widgets(self):        
        self.assignments_list_frame = ctk.CTkScrollableFrame(self)
        self.assignments_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_assignment_bars()
        
    def create_assignment_bars(self):
        if not self.assignments:
            no_assignments_label = ctk.CTkLabel(self.assignments_list_frame, text="No assignments available to grade", fg_color="#3B3B3B")
            no_assignments_label.pack(pady=20, fill="x")
            return

        for index, assignment in enumerate(self.assignments):
            assignment_frame = ctk.CTkFrame(self.assignments_list_frame, fg_color="#3B3B3B")
            assignment_frame.pack(fill="x", padx=10, pady=5)

            assignment_label = ctk.CTkLabel(assignment_frame, text=f"{index + 1}. {assignment.title}", anchor="w", fg_color="#3B3B3B")
            assignment_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            view_button = ctk.CTkButton(assignment_frame, text="View", width=80)
            view_button.pack(side="right", padx=10, pady=5)
            view_button.configure(command=lambda a=assignment: self.view_assignment(a))
            
    def view_assignment(self, assignment):
        self.master.hide_navigation_buttons()
        self.master.hide_back_button()
        self.hide_page()
        self.create_assignment_page(assignment)
        
    def create_assignment_page(self, assignment):
        if not hasattr(self, 'assignment_page'):
            self.master.assignment_list = self  # Store reference to AssignmentList
            self.assignment_page = AssignmentPage(self.master, self.user, assignment, self.on_assignment_complete)
        else:
            self.assignment_page.pack_forget()
            self.assignment_page = AssignmentPage(self.master, self.user, assignment, self.on_assignment_complete)
        self.assignment_page.show_page()

    def on_assignment_complete(self):
        self.hide_page()
        self.master.show_navigation_buttons()
        self.master.show_back_button()
        self.master.show_assignments()

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'assignment_page'):
            self.assignment_page.hide_page()

# if __name__ == "__main__":
#     root = ctk.CTk()
#     assignment_list = AssignmentList(root, None, None)
#     assignment_list.pack(fill="both", expand=True)
#     root.mainloop()

