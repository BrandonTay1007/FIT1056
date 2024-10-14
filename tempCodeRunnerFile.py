       
    sidebar = Sidebar(root)
    sidebar.pack(side="left", fill="y", padx=20, pady=20)
    
    # Create and pack the profile page
    profile_page = ProfilePage(root, test_user)
    profile_page.pack(side="left", fill="both", expand=True, padx=20, pady=20)