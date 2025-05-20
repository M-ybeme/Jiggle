# Mouse Jiggler

Mouse Jiggler is a simple tool that moves your mouse and optionally clicks to prevent your computer from going idle. It's built with Python and packaged as a single .exe file for Windows that doesn't require installation or admin rights.

## Features

* Move the mouse cursor at custom X and Y distances
* Click at a custom rate (clicks per minute)
* Set how long the app should run
* Pause and resume during operation
* Shows remaining time in hours\:minutes\:seconds
* Easy-to-use graphical interface (GUI)

## How to Use (Windows)

1. Run `MouseJiggle.exe` from the `dist` folder.
2. Enter:

   * How long to run (in minutes)
   * X and Y movement distances
   * How many clicks per minute (optional)
3. Click "Start" to begin.
4. Use the buttons to Pause, Resume, Stop, or toggle clicking on/off.

The app will update the progress bar and remaining time as it runs.

## File Structure

```
MouseJiggler/
├── dist/
│   └── MouseJiggle.exe         # The file you run (Windows)
├── MouseJigglerLogo.png        # GUI image
├── MouseJigglerLogo2.png       # Image while running
├── MouseFavicon.ico            # App icon
├── MouseJiggle.py              # Source code (for developers)
├── README.md                   # This file
```

## Notes

* No installation needed
* No changes made to your system
* May be flagged by antivirus since it's unsigned

## Developers

Requirements:

* Python 3
* `pyautogui`

Install dependencies:

```bash
pip install pyautogui
```

Run from source:

```bash
python MouseJiggle.py
```

### Build on Windows with PyInstaller

```bash
pyinstaller --onefile --windowed --icon=MouseFavicon.ico \
--add-data "MouseFavicon.ico;." \
--add-data "MouseJigglerLogo.png;." \
--add-data "MouseJigglerLogo2.png;." \
MouseJiggle.py
```

### Optional: Build on macOS with py2app

If you want to build a macOS-compatible `.app` bundle:

1. Install py2app:

```bash
pip install py2app
```

2. Create a `setup.py`:

```python
from setuptools import setup

APP = ['MouseJiggle.py']
DATA_FILES = ['MouseFavicon.ico', 'MouseJigglerLogo.png', 'MouseJigglerLogo2.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'MouseFavicon.icns',  # Convert .ico to .icns for macOS
    'packages': ['pyautogui'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

3. Build the app:

```bash
python setup.py py2app
```

4. Distribute `dist/MouseJiggle.app` via `.zip`.

Note: macOS may block the app unless it's signed and notarized through an Apple Developer account.

## License

MIT License
