import os
import random
import time
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("Mero Music Player")
root.geometry("500x300")
root.configure(bg="#6a0dad")  # Set background color to purple

# Create labels
current_song = tk.StringVar()
status = tk.StringVar()
current_song_label = tk.Label(root, textvariable=current_song, font=("Helvetica", 14), bg="#6a0dad", fg="white")  # Set label background and text color
status_label = tk.Label(root, textvariable=status, font=("Helvetica", 12), bg="#6a0dad", fg="white")  # Set label background and text color

# Create buttons
def play_music():
    pygame.mixer.music.unpause()
    status.set("Music playing...")

def pause_music():
    pygame.mixer.music.pause()
    status.set("Music paused...")

def stop_music():
    pygame.mixer.music.stop()
    status.set("Music stopped...")
    current_song.set("")

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        current_song.set(os.path.basename(file_path))
        status.set("Music playing...")

play_button = tk.Button(root, text="Play", command=play_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)
choose_button = tk.Button(root, text="Choose Song", command=choose_file)

# Position labels and buttons
current_song_label.pack(pady=10)
status_label.pack()
play_button.pack(side=tk.LEFT, padx=20, pady=20)
pause_button.pack(side=tk.LEFT, padx=20, pady=20)
stop_button.pack(side=tk.LEFT, padx=20, pady=20)
choose_button.pack(side=tk.LEFT, padx=20, pady=20)

# Create volume slider
def set_volume(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume, bg="#6a0dad", fg="white", highlightthickness=0, troughcolor="#FFFFFF", bd=0, activebackground="#FFFFFF", sliderrelief=tk.FLAT, sliderlength=20)  # Customize volume slider

# Position volume slider
volume_slider.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=10)

# Run the main window
root.mainloop()
