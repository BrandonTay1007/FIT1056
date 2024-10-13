import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root=ctk.CTk()
root.title("Add New User Page")
root.geometry("600x700")

#title
title_label=ctk.CTkLabel(root, text="Add User", font=('Arial', 24, "bold"))
title_label.pack(pady=20)

#position selection
position_var=ctk.StringVar(value="Please select the position")
positions=["Teacher", "Student"]

position_label=ctk.CTkLabel(root, text="Position/role:")
position_label.pack(pady=10)

position_menu=ctk.CTkOptionMenu(root, variable=position_var, values=positions, state="readonly")
position_menu.pack()

#teacher/student ID
teacher_student_id_label=ctk.CTkLabel(root, text="TeacherID/StudentID:")
teacher_student_id_label.pack(pady=10)

teacher_student_id_entry=ctk.CTkEntry(root)
teacher_student_id_entry.pack()

#first name
first_name_label=ctk.CTkLabel(root, text="First Name:")
first_name_label.pack(pady=10)
first_name_entry=ctk.CTkEntry(root)
first_name_entry.pack()

#last name
last_name_label=ctk.CTkLabel(root, text="Last Name:")
last_name_label.pack(pady=10)
last_name_entry=ctk.CTkEntry(root)
last_name_entry.pack()

#contact number
contact_number_label=ctk.CTkLabel(root, text="Contact Number:")
contact_number_label.pack(pady=10)
contact_number_entry=ctk.CTkEntry(root)
contact_number_entry.pack()

#instrument selection
instrument_var=ctk.StringVar(value="Please select an instrument")
intruments=["Piano", "Flute", "Cello", "Violin", "Viola"]

instrument_label=ctk.CTkLabel(root, text="Instrument selection (teach / learn):")
instrument_label.pack(pady=10)
instrument_menu=ctk.CTkOptionMenu(root, variable=instrument_var, values=intruments, state="readonly")
instrument_menu.pack()

#"add" button
add_button=ctk.CTkButton(root, text="Add")
add_button.pack(pady=30)

root.mainloop()