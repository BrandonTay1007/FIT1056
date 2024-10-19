import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class PostPage(ctk.CTkFrame):
    def __init__(self, master, user, post, on_close_callback):
        super().__init__(master)
        self.master = master
        self.user = user
        self.post = post
        self.on_close_callback = on_close_callback
        self.configure(fg_color="transparent")
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = ctk.CTkLabel(self, text=self.post.title, font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(fill="x", padx=10, pady=10)
        
        # Author
        author_label = ctk.CTkLabel(self, text=f"Posted by {self.post.author}", font=ctk.CTkFont(size=12))
        author_label.pack(anchor="w", padx=10)
        
        # Content
        content_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        content_label = ctk.CTkLabel(content_frame, text=self.post.content, wraplength=500, justify="left")
        content_label.pack(padx=10, pady=10)
        
        # Comments section
        comments_label = ctk.CTkLabel(self, text="Comments", font=ctk.CTkFont(size=18, weight="bold"))
        comments_label.pack(anchor="w", padx=10, pady=(20, 10))
        
        self.comments_frame = ctk.CTkScrollableFrame(self)
        self.comments_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.create_comment_widgets()
        
        # Add comment input
        self.comment_input = ctk.CTkEntry(self, placeholder_text="Add a comment...")
        self.comment_input.pack(fill="x", padx=10, pady=(10, 0))
        
        comment_button = ctk.CTkButton(self, text="Comment", command=self.add_comment)
        comment_button.pack(anchor="e", padx=10, pady=10)
        
        # Back button
        back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button_click)
        back_button.pack(side="bottom", padx=10, pady=10)
        
    def create_comment_widgets(self):
        print(self.post.comments)
        for comment in self.post.comments:
            comment_frame = ctk.CTkFrame(self.comments_frame, fg_color="#3B3B3B")
            comment_frame.pack(fill="x", padx=5, pady=5)
            
            author_label = ctk.CTkLabel(comment_frame, text=comment.author, font=ctk.CTkFont(size=12, weight="bold"))
            author_label.pack(anchor="w", padx=5, pady=(5, 0))
            
            content_label = ctk.CTkLabel(comment_frame, text=comment.content, wraplength=450, justify="left")
            content_label.pack(anchor="w", padx=5, pady=(0, 5))
    
    def add_comment(self):
        comment_text = self.comment_input.get()
        if comment_text:
            new_comment = {
                "content": comment_text,
                "author_id": self.user.id,
                "author_name": self.user.username
            }
            self.post.add_comment(new_comment)
            self.comment_input.delete(0, 'end')
            self.refresh_comments()
    
    def refresh_comments(self):
        for widget in self.comments_frame.winfo_children():
            widget.destroy()
        self.create_comment_widgets()
    
    def on_back_button_click(self):
        self.hide_page()
        self.on_close_callback()
    
    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()

# if __name__ == "__main__":
#     root = ctk.CTk()
#     sample_post = {
#         "id": 1,
#         "title": "Sample Post",
#         "content": "This is a sample post content.",
#         "comments": [
#             {"id": 1, "content": "Great post!", "author_id": 2, "author_name": "Jane Doe"}
#         ],
#         "author_id": 1,
#         "author_name": "John Smith"
#     }
#     post_page = PostPage(root, None, sample_post, lambda: print("Closed"))
#     post_page.pack(fill="both", expand=True)
#     root.mainloop()

