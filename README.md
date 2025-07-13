Mouse Jiggler
Mouse Jiggler is a lightweight tool that simulates user activity by moving the mouse and optionally clicking. It's designed to prevent your system from going idle or locking due to inactivity. The app runs as a standalone .exe on Windows—no installation or admin rights required.

Features
Custom X and Y movement distances

Optional clicking at a specified rate (clicks per minute)

Configurable runtime duration

Pause and resume support

Real-time countdown and progress bar

Clean and simple graphical interface (built with ttkbootstrap)

System tray integration with quick start and show/hide options

Emergency stop via Ctrl + Shift + Esc

How to Use (Windows)
Run MouseJiggle.exe (located in the dist/ folder).

Configure:

Duration in minutes

Start and end times (24-hour format)

X and Y movement distances

Click rate (optional)

Click Start to begin.

Use the Pause, Resume, Stop, and Clicker Toggle buttons as needed.

The app continues running in the system tray and can be re-opened or auto-started for 1 hour from the tray menu.

File Structure

MouseJiggler/
├── dist/
│   └── MouseJiggle.exe         # Compiled Windows executable
├── MouseJiggle.py              # Source code (for developers)
├── MouseFavicon.ico            # Tray and app icon
├── MouseJigglerLogo.png        # Default app logo
├── MouseJigglerLogo2.png       # "Running" state logo
├── README.md                   # This file
Notes
No installation required

No changes are made to your system

May be flagged by antivirus due to unsigned executable (false positive)

For Developers
Requirements
Python 3.10 or higher

Packages:

pyautogui

ttkbootstrap

pystray

Pillow

keyboard

Install Dependencies

pip install pyautogui ttkbootstrap pystray Pillow keyboard
Run from Source

python MouseJiggle.py
Building the App with PyInstaller (Windows)
To package it as a standalone .exe:


pyinstaller --onefile --windowed --icon=MouseFavicon.ico ^
  --add-data "MouseFavicon.ico;." ^
  --add-data "MouseJigglerLogo.png;." ^
  --add-data "MouseJigglerLogo2.png;." ^
  MouseJiggle.py
⚠️ On PowerShell, you may need to run with full path or fix your PATH if pyinstaller is not recognized.

macOS Support (Optional)
This project is designed for Windows, but you can experiment with macOS support using py2app. This is not officially supported and will require extra signing steps to run.

License
MIT License
