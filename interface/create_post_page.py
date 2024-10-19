import customtkinter as ctk
from app.forum import Forum

class CreatePostPage(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.forum = Forum()
        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Create New Post", font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(20, 10))

        self.title_entry = ctk.CTkEntry(self, placeholder_text="Enter post title", width=300)
        self.title_entry.pack(pady=10)

        self.content_text = ctk.CTkTextbox(self, width=300, height=200)
        self.content_text.pack(pady=10)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)

        create_button = ctk.CTkButton(button_frame, text="Create Post", command=self.create_post)
        create_button.pack(side="left", padx=10)

        back_button = ctk.CTkButton(button_frame, text="Back", command=self.on_back)
        back_button.pack(side="left", padx=10)

    def on_back(self):
        self.hide_page()
        self.master.forum_list.refresh_posts()
        self.master.forum_list.show_page()

    def create_post(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", "end-1c")
        if title and content:
            self.forum.create_post(title, content, self.user)
            self.clear_fields()
            self.on_back()
        else:
            # Show an error message if title or content is empty
            error_label = ctk.CTkLabel(self, text="Please enter both title and content", text_color="red")
            error_label.pack(pady=10)
            self.after(3000, error_label.destroy)  # Remove error message after 3 seconds

    def clear_fields(self):
        self.title_entry.delete(0, "end")
        self.content_text.delete("1.0", "end")

    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
