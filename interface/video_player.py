import cv2
import customtkinter as ctk  # Changed to import ctk
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, frame, video_title, video_path):
        self.master = frame  # Use the provided frame instead of creating a new Tk instance

        video_title = ctk.CTkLabel(self.master, text=video_title, font=("Arial", 16, "bold"))  # Changed to ctk.CTkLabel with bigger and bold font
        video_title.pack()  # Corrected to pack the label directly

        self.canvas = ctk.CTkCanvas(self.master)  # Changed to ctk.CTkCanvas
        self.canvas.pack()  # Corrected to pack the canvas directly

        self.progress_slider = ctk.CTkSlider(self.master, from_=0, to=1, command=self.seek_video)  # Added progress slider
        self.progress_slider.pack(fill=ctk.X, padx=10, pady=10)  # Pack the slider above the buttons

        self.play_button = ctk.CTkButton(self.master, text="Play", command=self.play_video)  # Changed to ctk.CTkButton
        self.play_button.pack(pady=10)

        self.pause_button = ctk.CTkButton(self.master, text="Pause", command=self.pause_video)  # Changed to ctk.CTkButton
        self.pause_button.pack(pady=10)

        self.cap = cv2.VideoCapture(video_path)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas.config(width=self.width, height=self.height)

        self.paused = True  # Ensure paused is set to True by default
        self.time_label = ctk.CTkLabel(self.master, text="0:00 / 0:00")  # Added label for time display
        self.time_label.pack(pady=5)  # Pack the label

        self.update()

    def play_video(self):
        self.paused = False

    def pause_video(self):
        self.paused = True

    def update(self):
        if not self.paused:
            ret, frame = self.cap.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)  # Changed to ctk.NW
                
                # Update the slider position based on the current frame
                current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
                self.progress_slider.set(current_frame / total_frames)  # Update slider position

                # Calculate current time and total duration
                current_time = self.cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Current time in seconds
                total_time = total_frames / self.cap.get(cv2.CAP_PROP_FPS)  # Total duration in seconds
                self.time_label.configure(text=f"{self.format_time(current_time)} / {self.format_time(total_time)}")  # Update label text

        self.master.after(10, self.update)  # Changed from self.root to self.master

    def seek_video(self, value):
        # Seek to the specified position in the video
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_to_seek = int(float(value) * total_frames)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_seek)  # Set the video to the new frame

    def format_time(self, seconds):
        # Format time in minutes:seconds
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes}:{seconds:02d}"  # Format as MM:SS

if __name__ == "__main__":
    root = ctk.CTk()
    player = VideoPlayer(root, "Video Player", "database/videos/testing.mp4")
    root.mainloop()
