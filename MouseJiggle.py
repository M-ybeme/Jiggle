import sys
import os
# Check if the script is running in a virtual environment

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from threading import Thread

# Define the Jiggler class
class Jiggler:
    def __init__(self):
        self.running = False
        self.paused = False
        self.elapsed_time = 0
        self.duration = 0
        self.clicking = False
        self.last_position = pyautogui.position()

    def toggle_click(self):
        self.clicking = not self.clicking
        click_button.config(text="Clicker On" if self.clicking else "Clicker Off")

    def toggle_pause(self):
        self.paused = not self.paused
        pause_button.config(text="Resume" if self.paused else "Pause")

    def start_jiggle(self, duration, x_distance, y_distance, clicks_per_minute):
        self.running = True
        self.duration = duration
        logo_image_running = tk.PhotoImage(file=resource_path('MouseJigglerLogo2.png'))
        resized_logo_image_running = logo_image_running.subsample(2, 2)
        logo_label.config(image=resized_logo_image_running)
        logo_label.image = resized_logo_image_running
        start_time = time.time()
        click_interval = 60 / clicks_per_minute
        last_click_time = time.time()
        last_movement_time = time.time()
        while (time.time() - start_time) < duration and self.running:
            if not self.paused:
                pyautogui.move(x_distance, y_distance)
                if self.clicking and time.time() - last_click_time >= click_interval:
                    pyautogui.click()
                    last_click_time = time.time()
                pyautogui.move(-x_distance, -y_distance)
                if self.clicking and time.time() - last_click_time >= click_interval:
                    pyautogui.click()
                    last_click_time = time.time()
            time.sleep(1)
            self.elapsed_time = time.time() - start_time
            current_position = pyautogui.position()
            if current_position != self.last_position:
                self.clicking = False
                last_movement_time = time.time()
                self.last_position = current_position
            elif time.time() - last_movement_time >= 5:
                self.clicking = True
        root.after(0, self.stop_jiggle)

    def stop_jiggle(self):
        self.running = False
        self.elapsed_time = 0
        logo_label.config(image=resized_logo_image)
        logo_label.image = resized_logo_image
        progress_var.set(0)

def update_progress():
    if jiggler.running and not jiggler.paused:
        # Update progress bar
        progress = int((jiggler.elapsed_time / jiggler.duration) * 100) if jiggler.duration > 0 else 0
        progress_var.set(progress)

        # Total time breakdown
        total_seconds = int(jiggler.duration)
        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60
        total_time_label.config(text=f"Total Time: {total_hours} hour(s) {total_minutes} minute(s)")

        # Remaining time in h:mm:ss
        remaining_seconds = int(jiggler.duration - jiggler.elapsed_time)
        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60
        remaining_time = f"{hours}:{minutes:02}:{seconds:02}"
        remaining_time_label.config(text=f"Remaining Time: {remaining_time}")

    root.after(1000, update_progress)


def start_jiggler(event=None):
    try:
        duration = int(duration_entry.get()) * 60
        x_distance = int(x_distance_entry.get())
        y_distance = int(y_distance_entry.get())
        clicks_per_minute = int(clicks_entry.get())
        if clicks_per_minute <= 0:
            raise ValueError
        Thread(target=jiggler.start_jiggle, args=(duration, x_distance, y_distance, clicks_per_minute)).start()
    except ValueError:
        error_label.config(text="Invalid input. Please enter a valid number.")
        duration_entry.delete(0, tk.END)
        x_distance_entry.delete(0, tk.END)
        y_distance_entry.delete(0, tk.END)
        clicks_entry.delete(0, tk.END)
        root.after(5000, lambda: error_label.config(text=""))

def stop_jiggler():
    jiggler.stop_jiggle()

def toggle_click():
    jiggler.toggle_click()

def toggle_pause():
    jiggler.toggle_pause()

jiggler = Jiggler()
root = tk.Tk()
root.title("Mouse Jiggler")
root.iconbitmap(resource_path('MouseFavicon.ico'))

logo_image = tk.PhotoImage(file=resource_path('MouseJigglerLogo.png'))
resized_logo_image = logo_image.subsample(2, 2)
logo_label = tk.Label(root, image=resized_logo_image)
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

duration_frame = tk.Frame(root)
duration_frame.grid(row=1, column=0, padx=10, pady=10)
duration_label = tk.Label(duration_frame, text="Duration (minutes):")
duration_label.pack(side=tk.LEFT)
duration_entry = tk.Entry(duration_frame)
duration_entry.pack(side=tk.LEFT)
duration_entry.bind('<Return>', start_jiggler)

direction_frame = tk.Frame(root)
direction_frame.grid(row=2, column=0, padx=10, pady=10)
jiggle_direction_label = tk.Label(direction_frame, text="Enter the X and Y distances for the mouse to move:")
jiggle_direction_label.pack()
x_distance_label = tk.Label(direction_frame, text="X Distance:")
x_distance_label.pack()
x_distance_entry = tk.Entry(direction_frame)
x_distance_entry.insert(0, "1")
x_distance_entry.pack()
x_distance_entry.bind('<Return>', start_jiggler)
y_distance_label = tk.Label(direction_frame, text="Y Distance:")
y_distance_label.pack()
y_distance_entry = tk.Entry(direction_frame)
y_distance_entry.insert(0, "1")
y_distance_entry.pack()
y_distance_entry.bind('<Return>', start_jiggler)

clicks_frame = tk.Frame(root)
clicks_frame.grid(row=3, column=0, padx=10, pady=10)
clicks_label = tk.Label(clicks_frame, text="Clicks per minute:")
clicks_label.pack(side=tk.LEFT)
clicks_entry = tk.Entry(clicks_frame)
clicks_entry.insert(0, "1")
clicks_entry.pack(side=tk.LEFT)
clicks_entry.bind('<Return>', start_jiggler)

button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, padx=10, pady=10)
start_button = tk.Button(button_frame, text="Start", command=start_jiggler, bg='green', fg='white')
start_button.pack(side=tk.LEFT, padx=5)
stop_button = tk.Button(button_frame, text="Stop", command=stop_jiggler, bg='red', fg='white')
stop_button.pack(side=tk.LEFT, padx=5)
click_button = tk.Button(button_frame, text="Clicker Off", command=toggle_click)
click_button.pack(side=tk.LEFT, padx=5)
pause_button = tk.Button(button_frame, text="Pause", command=toggle_pause)
pause_button.pack(side=tk.LEFT, padx=5)
error_label = tk.Label(root, text="")
error_label.grid(row=5, column=0, padx=10, pady=10)

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=200, mode='determinate', variable=progress_var)
progress_bar.grid(row=8, column=0, padx=10, pady=10)

time_labels_frame = tk.Frame(root)
time_labels_frame.grid(row=6, column=0, padx=10, pady=5)
total_time_label = tk.Label(time_labels_frame, text="Total Time: 0 hour(s)")
total_time_label.pack(side=tk.LEFT, padx=10)
remaining_time_label = tk.Label(time_labels_frame, text="Remaining Time: 00:00")
remaining_time_label.pack(side=tk.LEFT, padx=10)

root.after(1000, update_progress)
root.mainloop()
