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

Let me know if you’d like a version that’s installer-ready (e.g., .exe packaged with Inno Setup or NSIS), or if you want the app to run silently in the background with tray support.







You said:
Can you make it markdown friendly for github?


ChatGPT said:
Absolutely — here is the updated GitHub-flavored Markdown version of your README.md, ready to drop into your project root on GitHub or in any markdown viewer:

markdown
Copy
Edit
# 🖱️ Mouse Jiggler

**Mouse Jiggler** is a lightweight Windows utility that prevents your computer from going idle by gently moving the mouse cursor and optionally performing automatic clicks. It’s distributed as a standalone executable — **no installation or admin privileges required.**

---

## 🔧 Features

- Custom mouse movement in **X and Y** directions
- Optional **auto-clicking** at a user-defined rate (clicks per minute)
- Adjustable **session duration**
- **Pause/resume** control during operation
- **Real-time progress bar**
- Displays **remaining time in `H:MM:SS` format**
- Distributed as a **standalone GUI `.exe`** — no Python or setup needed

---

## 📁 Folder Structure (After Build)

If you're building or distributing the app manually:

MouseJiggler/
├── dist/
│ └── MouseJiggle.exe # The standalone executable
├── MouseJigglerLogo.png # GUI logo image (bundled)
├── MouseJigglerLogo2.png # Alternate image shown when running
├── MouseFavicon.ico # App window icon
├── MouseJiggle.py # Source code (for devs)
├── README.md # This file

markdown
Copy
Edit

When built using `pyinstaller --onefile`, all assets are embedded inside `MouseJiggle.exe`.

---

## 🚀 How to Use

### 🧑‍💻 As an End User:
1. Run `MouseJiggle.exe` from the `dist/` folder.
2. Configure the following in the GUI:
   - **Duration (minutes):** Total time the app should run.
   - **X Distance / Y Distance:** How far the mouse moves in each direction.
   - **Clicks per Minute:** (Optional) How often to perform mouse clicks.
3. Use the buttons to:
   - **Start** / **Stop**
   - Toggle **Clicker On/Off**
   - **Pause** / **Resume**
4. Watch the **progress bar** and **remaining time countdown**.

> ⏱ Remaining time displays in `H:MM:SS`. Total time is shown in hours and minutes.

---

### 🧪 As a Developer:
To run from source:

#### 📦 Requirements:
- Python 3.10+
- `pyautogui`, `tkinter` (usually comes with Python)

#### 🧰 Installation:
```bash
pip install pyautogui
▶️ Run:
bash
Copy
Edit
python MouseJiggle.py
🔒 Security & Execution
✅ Does not require admin rights

✅ Does not modify registry or protected system folders

✅ Can be run from Downloads, Documents, or %AppData%

⚠️ Note: On some corporate laptops, antivirus software may flag unsigned .exe files. If this happens:

Move the .exe to a less restricted directory (e.g. C:\Users\YourName\AppData\Local)

Or ask IT to review and whitelist it

🛠 Build Instructions (PyInstaller)
If you want to rebuild the .exe:

bash
Copy
Edit
pyinstaller --onefile --windowed --icon=MouseFavicon.ico ^
--add-data "MouseFavicon.ico;." ^
--add-data "MouseJigglerLogo.png;." ^
--add-data "MouseJigglerLogo2.png;." ^
MouseJiggle.py
Or on one line for PowerShell:

powershell
Copy
Edit
pyinstaller --onefile --windowed --icon=MouseFavicon.ico --add-data "MouseFavicon.ico;." --add-data "MouseJigglerLogo.png;." --add-data "MouseJigglerLogo2.png;." MouseJiggle.py
📄 License
This project is licensed under the MIT License.
