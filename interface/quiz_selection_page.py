import customtkinter as ctk
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app.user import User

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class QuizMenu(ctk.CTk):
    def __init__(self, user, tutor, admin):
        self.user = user
        self.tutor = tutor
        self.admin = admin

        #when user is Learner
        if isinstance(self.user, User):
            self.title = ctk.CTkLabel(self, text = "Welcome to Quiz Selection", font = ('Arial Bold',30))
            self.title.grid(row = 1, columnspan = 2, padx = 10, pady = 30, sticky = ctk.W+ctk.E)

            self.create_q = ctk.CTkButton(self, text = "Python Programming", font = ('Arial Bold',20))
            self.create_q.grid(row = 2, columnspan = 2, padx = 70, pady = 10, sticky = ctk.W+ctk.E)

            self.view_q = ctk.CTkButton(self, text = "Artificial intelligence", font = ('Arial Bold',20))
            self.view_q.grid(row = 3, columnspan = 2, padx = 70, pady = 10, sticky = ctk.W+ctk.E)

            self.delete_q = ctk.CTkButton(self, text = "Extra Quiz", font = ('Arial Bold',20))
            self.delete_q.grid(row = 4, columnspan = 2, padx = 70, pady = 10, sticky = ctk.W+ctk.E)


            self.back_button = ctk.CTkButton(self, text = "Back", font = ('Arial Bold',20))
            self.back_button.grid(pady = 100, sticky = ctk.S+ctk.W)
    
        #when user is Tutor or Admin
        else:
            self.title = ctk.CTkLabel(self, text = "Quiz Menu", font = ('Arial Bold',30))
            self.title.grid(row = 1, columnspan = 2, padx = 10, pady = 30, sticky = ctk.W+ctk.E)

            self.create_q = ctk.CTkButton(self, text = "Create Quiz", font = ('Arial Bold',20))
            self.create_q.grid(row = 2, columnspan = 2, padx = 70, pady = 10, sticky = ctk.W+ctk.E)

            self.view_q = ctk.CTkButton(self, text = "View Quiz", font = ('Arial Bold',20))
            self.view_q.grid(row = 3, columnspan = 2, padx = 70, pady = 10, sticky = ctk.W+ctk.E)
            

            self.back_button = ctk.CTkButton(self, text = "Back", font = ('Arial Bold',20))
            self.back_button.grid(pady = 100, sticky = ctk.S+ctk.W)



    root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Quiz Selection")
    root.geometry("600x700")
    root.minsize(600, 700)  # Set minimum window size
    u = User(1, "JohnDoe", "password", "John", "Doe", "learner", "tseting", "testing", "testing", "testing")    
    quiz_selection_page = QuizMenu(root, u, u, u)
    root.mainloop()


