import customtkinter as ctk
from app.forum import Forum
from interface.post_page import PostPage
from interface.create_post_page import CreatePostPage

class ForumList(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.master = master
        self.user = user
        self.forum = Forum()
        self.configure(fg_color="transparent")
        self.create_widgets()
        self.master.forum_list = self

    def create_widgets(self):
        title_bar = ctk.CTkLabel(self, text="Discussion Forum", font=ctk.CTkFont(size=24, weight="bold"))
        title_bar.pack(fill="x", padx=10, pady=10)
        
        self.posts_list_frame = ctk.CTkScrollableFrame(self)
        self.posts_list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 50))
        
        self.create_post_bars()
        self.create_button_frame()

    def create_button_frame(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", side="bottom", padx=10, pady=10)

        button_container = ctk.CTkFrame(button_frame, fg_color="transparent")
        button_container.pack(side="left")

        self.create_post_button = ctk.CTkButton(button_container, text="Create New Post", command=self.create_new_post)
        self.create_post_button.pack(pady=(0, 10))  # Add padding to the bottom
        
        self.back_button = ctk.CTkButton(button_container, text="Back", command=self.on_back_button_click)
        self.back_button.pack()

    def create_post_bars(self):
        posts = self.forum.get_posts()
        if not posts:
            no_posts_label = ctk.CTkLabel(self.posts_list_frame, text="No posts available", fg_color="#3B3B3B")
            no_posts_label.pack(pady=20, fill="x")
            return

        for index, post in enumerate(posts):
            post_frame = ctk.CTkFrame(self.posts_list_frame, fg_color="#3B3B3B")
            post_frame.pack(fill="x", padx=10, pady=5)

            post_label = ctk.CTkLabel(post_frame, text=f"{index + 1}. {post.title}", anchor="w", fg_color="#3B3B3B")
            post_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            view_button = ctk.CTkButton(post_frame, text="View", width=80)
            view_button.pack(side="right", padx=10, pady=5)
            view_button.configure(command=lambda p=post: self.view_post(p))
            
    def view_post(self, post):
        self.hide_page()
        self.create_post(post)
        
    def create_post(self, post):
        if not hasattr(self, 'post_page'):
            self.master.forum_list = self  # Store reference to ForumList
            self.post_page = PostPage(self.master, self.user, post, self.on_post_close)
        else:
            self.post_page.pack_forget()
            self.post_page = PostPage(self.master, self.user, post, self.on_post_close)
        self.post_page.show_page()

    def on_post_close(self):
        self.hide_page()
        self.show_page()

    def on_back_button_click(self):
        self.hide_page()
        self.user.menu.show_page()
    
    def show_page(self):
        self.pack(fill="both", expand=True)

    def hide_page(self):
        self.pack_forget()
        if hasattr(self, 'post_page'):
            self.post_page.hide_page()

    def refresh_posts(self):
        # Clear existing widgets in the scrollable frame
        for widget in self.posts_list_frame.winfo_children():
            widget.destroy()
        self.forum.posts = []
        # Refresh the forum posts data
        self.forum.init_posts()
        # Recreate the post bars
        self.create_post_bars() 
        
    def create_new_post(self):
        self.hide_page()
        if not hasattr(self, 'create_post_page'):
            self.create_post_page = CreatePostPage(self.master, self.user)
        self.create_post_page.show_page()
