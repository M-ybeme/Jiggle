Mouse Jiggler
Mouse Jiggler is a lightweight Windows utility that prevents your computer from going idle by gently moving the mouse cursor and optionally performing automatic clicks. It’s distributed as a standalone executable—no installation or admin privileges required.

🔧 Features
Custom mouse movement in X and Y directions

Optional auto-clicking at a user-defined rate (clicks per minute)

Adjustable session duration

Pause/resume functionality during operation

Real-time progress bar

Remaining time displayed in H:MM:SS format

Standalone GUI executable — no Python required

📦 Folder Structure (Post-Build)
After building or downloading:

css
Copy
Edit
MouseJiggler/
├── dist/
│   └── MouseJiggle.exe         ← The standalone executable to run
├── MouseJigglerLogo.png        ← Bundled GUI logo (auto-loaded in .exe)
├── MouseJigglerLogo2.png       ← Alternate running-state logo
├── MouseFavicon.ico            ← Application window icon
├── MouseJiggle.py              ← Source code (for developers)
├── README.txt                  ← This file
All assets are bundled inside MouseJiggle.exe using PyInstaller. Your friend only needs the .exe.

🚀 Usage
Run MouseJiggle.exe

No install required.

No admin privileges needed.

You can place the .exe in any folder, such as Documents or AppData.

Configure Settings in the GUI:

Duration (minutes) – how long the jiggling should last.

X Distance / Y Distance – pixel movement amount.

Clicks per Minute – optional click frequency.

Use the Start, Stop, Pause, and Clicker On/Off buttons to control behavior.

Progress Display

Shows total session time and a live countdown timer.

Time is displayed in H:MM:SS format.

⚠ Notes
Mouse movement and clicking is active during the session. Avoid using your mouse for other tasks unless paused.

The app detects manual user mouse movement and temporarily disables auto-clicking to prevent interference.

Built-in images and icons are auto-resolved at runtime and require no manual configuration.

🔒 Security & Permissions
This application:

Does not require installation

Does not write to registry or system folders

Can be safely run from any user-writable directory

Note: On some corporate laptops, antivirus software may flag unknown .exe files. If you encounter issues, try running from AppData or ask IT to whitelist it.

🛠 For Developers
Dependencies (if running from source):

Python 3.10+

pyautogui, tkinter

Install:

bash
Copy
Edit
pip install pyautogui
Run:

bash
Copy
Edit
python MouseJiggle.py
📄 License
This project is licensed under the MIT License. See LICENSE file if included.
