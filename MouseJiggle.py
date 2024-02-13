import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from threading import Thread

class Jiggler:
    def __init__(self):
        self.running = False
        self.elapsed_time = 0
        self.duration = 0

    def start_jiggle(self, duration, x_distance, y_distance):
        self.running = True
        self.duration = duration
        logo_image_running = tk.PhotoImage(file='MouseJigglerLogo2.png')  # load the second logo
        resized_logo_image_running = logo_image_running.subsample(2, 2)  # resize the running logo
        logo_label.config(image=resized_logo_image_running)  # change the logo
        logo_label.image = resized_logo_image_running  # keep a reference to the image
        start_time = time.time()
        while (time.time() - start_time) < duration and self.running:
            pyautogui.move(x_distance, y_distance)
            pyautogui.move(-x_distance, -y_distance)
            time.sleep(1)
            self.elapsed_time = time.time() - start_time
        root.after(0, self.stop_jiggle) # schedule stop_jiggle to run on the main thread after the loop ends
        

    def stop_jiggle(self):
        self.running = False
        logo_label.config(image=resized_logo_image)  # change the logo back to the original
        logo_label.image = resized_logo_image  # keep a reference to the image
        progress_var.set(0)  # reset the progress bar

def update_progress():
    if jiggler.running:
        progress_var.set(int((jiggler.elapsed_time / jiggler.duration) * 100))  # update progress bar
    root.after(1000, update_progress)  # schedule this function to run again after 1 second

def start_jiggler(event=None):  # add event parameter to handle key press event
    try:
        duration = int(duration_entry.get()) * 60  # convert minutes to seconds
        x_distance = int(x_distance_entry.get())
        y_distance = int(y_distance_entry.get())
        Thread(target=jiggler.start_jiggle, args=(duration, x_distance, y_distance)).start()
    except ValueError:
        error_label.config(text="Invalid input. Please enter a valid number.")
        # Clear the invalid input
        duration_entry.delete(0, tk.END)
        x_distance_entry.delete(0, tk.END)
        y_distance_entry.delete(0, tk.END)
        # Schedule the error message to be cleared after 5 seconds
        root.after(5000, lambda: error_label.config(text=""))

def stop_jiggler():
    jiggler.stop_jiggle()

jiggler = Jiggler()

root = tk.Tk()

root.title("Mouse Jiggler")

root.iconbitmap('MouseFavicon.ico')

logo_image = tk.PhotoImage(file='MouseJigglerLogo.png')
resized_logo_image = logo_image.subsample(2, 2)  # resize the image
logo_label = tk.Label(root, image=resized_logo_image)
logo_label.pack()

duration_label = tk.Label(root, text="Duration (minutes):")
duration_label.pack()

duration_entry = tk.Entry(root)
duration_entry.pack()
duration_entry.bind('<Return>', start_jiggler)  # bind Enter key to start_jiggler function

jiggle_direction_label = tk.Label(root, text="Enter the X and Y distances for the mouse to move:")
jiggle_direction_label.pack()

x_distance_label = tk.Label(root, text="X Distance:")
x_distance_label.pack()

x_distance_entry = tk.Entry(root)
x_distance_entry.insert(0, "1")  # set default value to 1
x_distance_entry.pack()
x_distance_entry.bind('<Return>', start_jiggler)  # bind Enter key to start_jiggler function

y_distance_label = tk.Label(root, text="Y Distance:")
y_distance_label.pack()

y_distance_entry = tk.Entry(root)
y_distance_entry.insert(0, "1")  # set default value to 1
y_distance_entry.pack()
y_distance_entry.bind('<Return>', start_jiggler)  # bind Enter key to start_jiggler function

start_button = tk.Button(root, text="Start", command=start_jiggler)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_jiggler)
stop_button.pack()

error_label = tk.Label(root, text="")
error_label.pack()

progress_var = tk.IntVar()  # create a variable to store the progress
progress_bar = ttk.Progressbar(root, length=200, mode='determinate', variable=progress_var)
progress_bar.pack()

root.after(1000, update_progress)  # start updating the progress bar
root.mainloop()