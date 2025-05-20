# Mouse Jiggler

Mouse Jiggler is a simple tool that moves your mouse and optionally clicks to prevent your computer from going idle. It's built with Python and packaged as a single .exe file that doesn't require installation or admin rights.

## Features

* Move the mouse cursor at custom X and Y distances
* Click at a custom rate (clicks per minute)
* Set how long the app should run
* Pause and resume during operation
* Shows remaining time in hours\:minutes\:seconds
* Easy-to-use graphical interface (GUI)

## How to Use

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
│   └── MouseJiggle.exe         # The file you run
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

Build with PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=MouseFavicon.ico \
--add-data "MouseFavicon.ico;." \
--add-data "MouseJigglerLogo.png;." \
--add-data "MouseJigglerLogo2.png;." \
MouseJiggle.py
```

## License

MIT License
