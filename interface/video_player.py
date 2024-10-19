import cv2
import customtkinter as ctk
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, frame, video_title, video_path):
        self.master = frame
        
        # Set up UI components
        video_title = ctk.CTkLabel(self.master, text=video_title, font=("Arial", 16, "bold"))
        video_title.pack()

        self.canvas = ctk.CTkCanvas(self.master)
        self.canvas.pack()

        self.progress_slider = ctk.CTkSlider(self.master, from_=0, to=1, command=self.seek_video)
        self.progress_slider.pack(fill=ctk.X, padx=10, pady=10)

        # Initialize video capture and properties
        self.cap = cv2.VideoCapture(video_path)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width=self.width, height=self.height)

        self.paused = True
        self.time_label = ctk.CTkLabel(self.master, text="0:00 / 0:00")
        self.time_label.pack(pady=5)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_time = int(1000 / self.fps)
        self.speed_factor = 1.0

        # Speed control
        self.speed_slider = ctk.CTkSlider(self.master, from_=0.25, to=2.0, number_of_steps=7, command=self.set_speed)
        self.speed_slider.set(1.0)
        self.speed_slider.pack(fill=ctk.X, padx=10, pady=5)

        self.speed_label = ctk.CTkLabel(self.master, text="Speed: 1.0x")
        self.speed_label.pack(pady=5)

        # Playback control buttons
        self.play_button = ctk.CTkButton(self.master, text="Play", command=self.play_video)
        self.play_button.pack(pady=10)

        self.pause_button = ctk.CTkButton(self.master, text="Pause", command=self.pause_video)
        self.pause_button.pack(pady=10)
        
        self.update()

    def play_video(self):
        self.paused = False

    def pause_video(self):
        self.paused = True

    def set_speed(self, value):
        self.speed_factor = float(value)
        self.speed_label.configure(text=f"Speed: {self.speed_factor:.2f}x")

    def update(self):
        if not self.paused:
            ret, frame = self.cap.read()
            if ret:
                # Convert frame to PhotoImage and display it
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)
                
                # Update progress slider and time label
                current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
                self.progress_slider.set(current_frame / total_frames)

                current_time = self.cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
                total_time = total_frames / self.fps
                self.time_label.configure(text=f"{self.format_time(current_time)} / {self.format_time(total_time)}")

        # Schedule next update based on playback speed
        adjusted_frame_time = int(self.frame_time / self.speed_factor)
        self.master.after(max(1, adjusted_frame_time), self.update)

    def seek_video(self, value):
        # Seek to the specified position in the video
        # The 'value' parameter is a float between 0 and 1, representing the progress
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_to_seek = int(float(value) * total_frames)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_seek)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes}:{seconds:02d}"