import sys
import os
import ctypes
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from threading import Thread
from datetime import datetime, timedelta
from PIL import Image
import pystray
import keyboard
import ttkbootstrap as tb


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_idle_duration():
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    last_input_info = LASTINPUTINFO()
    last_input_info.cbSize = ctypes.sizeof(last_input_info)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(last_input_info))
    millis = ctypes.windll.kernel32.GetTickCount() - last_input_info.dwTime
    return millis / 1000.0


class Jiggler:
    def __init__(self):
        self.running = False
        self.paused = False
        self.elapsed_time = 0
        self.duration = 0
        self.clicking = False

    def toggle_click(self):
        self.clicking = not self.clicking
        click_button.config(text="Clicker On" if self.clicking else "Clicker Off")

    def toggle_pause(self):
        self.paused = not self.paused
        pause_button.config(text="Resume" if self.paused else "Pause")

    def start_jiggle(self, duration, x_distance, y_distance, clicks_per_minute, sched_start, sched_end):
        self.running = True
        self.duration = duration
        logo_image_running = tk.PhotoImage(file=resource_path('MouseJigglerLogo2.png'))
        resized_logo_image_running = logo_image_running.subsample(2, 2)
        logo_label.config(image=resized_logo_image_running)
        logo_label.image = resized_logo_image_running
        start_time = time.time()
        click_interval = 60 / clicks_per_minute
        last_click_time = time.time()

        while (time.time() - start_time) < duration and self.running:
            now = datetime.now().time()
            if now < sched_start or now > sched_end:
                time.sleep(5)
                continue

            idle_seconds = get_idle_duration()
            # Pause only if user has been active recently
            if idle_seconds < 30:
                if not self.paused:
                    self.paused = True
                    pause_button.config(text="Resume")
            else:
                if self.paused:
                    self.paused = False
                    pause_button.config(text="Pause")
            
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

        root.after(0, self.stop_jiggle)

    def stop_jiggle(self):
        self.running = False
        self.elapsed_time = 0
        logo_label.config(image=resized_logo_image)
        logo_label.image = resized_logo_image
        progress_var.set(0)


def update_progress():
    if jiggler.running and not jiggler.paused:
        progress = int((jiggler.elapsed_time / jiggler.duration) * 100) if jiggler.duration > 0 else 0
        progress_var.set(progress)

        total_seconds = int(jiggler.duration)
        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60
        total_time_label.config(text=f"Total Time: {total_hours} hour(s) {total_minutes} minute(s)")

        remaining_seconds = int(jiggler.duration - jiggler.elapsed_time)
        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60
        remaining_time_label.config(text=f"Remaining Time: {hours}:{minutes:02}:{seconds:02}")

    root.after(1000, update_progress)


def start_jiggler(event=None):
    try:
        duration = int(duration_entry.get()) * 60
        x_distance = int(x_distance_entry.get())
        y_distance = int(y_distance_entry.get())
        clicks_per_minute = int(clicks_entry.get())
        sched_start = datetime.strptime(start_time_entry.get(), "%H:%M").time()
        sched_end = datetime.strptime(end_time_entry.get(), "%H:%M").time()
        if clicks_per_minute <= 0:
            raise ValueError
        Thread(target=jiggler.start_jiggle, args=(duration, x_distance, y_distance, clicks_per_minute, sched_start, sched_end), daemon=True).start()
    except ValueError:
        error_label.config(text="Invalid input. Please enter a valid number.")
        root.after(5000, lambda: error_label.config(text=""))


def auto_start_jiggler(start_str, end_str):
    try:
        duration = 60 * 60  # 1 hour
        x_distance = int(x_distance_entry.get())
        y_distance = int(y_distance_entry.get())
        clicks_per_minute = int(clicks_entry.get())
        sched_start = datetime.strptime(start_str, "%H:%M").time()
        sched_end = datetime.strptime(end_str, "%H:%M").time()
        Thread(target=jiggler.start_jiggle, args=(duration, x_distance, y_distance, clicks_per_minute, sched_start, sched_end), daemon=True).start()
    except Exception as e:
        print(f"[Auto Start Error] {e}")


def stop_jiggler():
    jiggler.stop_jiggle()


def toggle_click():
    jiggler.toggle_click()


def toggle_pause():
    jiggler.toggle_pause()


def on_close():
    jiggler.running = False
    root.withdraw()


def setup_tray_icon():
    def on_quit(icon, item):
        icon.stop()
        root.after(0, root.destroy)

    def on_pause(icon, item):
        jiggler.toggle_pause()

    def on_stop(icon, item):
        jiggler.stop_jiggle()

    def on_open_app(icon, item):
        root.after(0, lambda: (root.deiconify(), root.lift()))

    def on_start_default(icon, item):
        now = datetime.now()
        start_str = now.strftime("%H:%M")
        end_str = (now + timedelta(hours=1)).strftime("%H:%M")
        root.after(0, lambda: auto_start_jiggler(start_str, end_str))

    image = Image.open(resource_path("MouseFavicon.ico"))
    menu = pystray.Menu(
        pystray.MenuItem("Open App", on_open_app),
        pystray.MenuItem("Start (1 Hour)", on_start_default),
        pystray.MenuItem("Pause/Resume", on_pause),
        pystray.MenuItem("Stop", on_stop),
        pystray.MenuItem("Quit", on_quit)
    )
    icon = pystray.Icon("mouse_jiggler", image, "Mouse Jiggler", menu)
    Thread(target=icon.run, daemon=True).start()


def listen_for_emergency_stop():
    keyboard.add_hotkey("ctrl+shift+esc", lambda: jiggler.stop_jiggle())
    keyboard.wait()


# THEME TOGGLE (Optional if you want it)
def toggle_theme():
    current = root.style.theme.name
    new_theme = "darkly" if current != "darkly" else "flatly"
    root.style.theme_use(new_theme)


# MAIN UI SETUP
jiggler = Jiggler()
root = tb.Window(themename="darkly")
root.protocol("WM_DELETE_WINDOW", on_close)
root.title("Mouse Jiggler")
root.iconbitmap(resource_path('MouseFavicon.ico'))

logo_image = tk.PhotoImage(file=resource_path('MouseJigglerLogo.png'))
resized_logo_image = logo_image.subsample(2, 2)
logo_label = ttk.Label(root, image=resized_logo_image)
logo_label.pack(pady=10)

def make_label(text): return ttk.Label(root, text=text)
def make_entry(default=""):
    entry = ttk.Entry(root)
    entry.insert(0, default)
    return entry

make_label("Duration (minutes):").pack()
duration_entry = make_entry(); duration_entry.pack()

make_label("Start Time (HH:MM, 24h):").pack()
start_time_entry = make_entry("09:00"); start_time_entry.pack()

make_label("End Time (HH:MM, 24h):").pack()
end_time_entry = make_entry("17:00"); end_time_entry.pack()

make_label("X Distance:").pack()
x_distance_entry = make_entry("1"); x_distance_entry.pack()

make_label("Y Distance:").pack()
y_distance_entry = make_entry("1"); y_distance_entry.pack()

make_label("Clicks per minute:").pack()
clicks_entry = make_entry("1"); clicks_entry.pack()

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)
ttk.Button(button_frame, text="Start", command=start_jiggler, bootstyle="success").pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Stop", command=stop_jiggler, bootstyle="danger").pack(side=tk.LEFT, padx=5)
click_button = ttk.Button(button_frame, text="Clicker Off", command=toggle_click); click_button.pack(side=tk.LEFT, padx=5)
pause_button = ttk.Button(button_frame, text="Pause", command=toggle_pause); pause_button.pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Toggle Theme", command=toggle_theme).pack(side=tk.LEFT, padx=5)

error_label = ttk.Label(root, text=""); error_label.pack(pady=10)
progress_var = tk.IntVar()
ttk.Progressbar(root, length=200, mode='determinate', variable=progress_var).pack(pady=10)

time_labels_frame = ttk.Frame(root); time_labels_frame.pack(pady=5)
total_time_label = ttk.Label(time_labels_frame, text="Total Time: 0 hour(s)"); total_time_label.pack(side=tk.LEFT, padx=10)
remaining_time_label = ttk.Label(time_labels_frame, text="Remaining Time: 00:00"); remaining_time_label.pack(side=tk.LEFT, padx=10)

# STARTUP
Thread(target=setup_tray_icon, daemon=True).start()
Thread(target=listen_for_emergency_stop, daemon=True).start()
root.after(1000, update_progress)
root.mainloop()
