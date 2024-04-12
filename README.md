# Mouse Jiggler

Mouse Jiggler is a Python application that jiggles your mouse cursor and performs clicks at a specified interval. This can be useful to prevent your computer from going to sleep or to automate repetitive clicking tasks.

## Features

- Jiggle mouse cursor at specified X and Y distances.
- Perform clicks at a specified rate (clicks per minute).
- Pause and resume jiggling and clicking.
- Set the duration for the jiggling and clicking.
- GUI for easy interaction.

## Dependencies

- Python 3
- pyautogui
- tkinter

## Usage

1. Clone the repository.
2. Install the dependencies: `pip install pyautogui tkinter`
3. Run the script: `python MouseJiggle.py`
4. Enter the desired parameters in the GUI and click "Start".

## GUI

The GUI includes fields for:

- Duration (minutes): The duration for which the mouse should be jiggled.
- X Distance: The distance in pixels the mouse should move along the X-axis.
- Y Distance: The distance in pixels the mouse should move along the Y-axis.
- Clicks per minute: The rate at which the mouse should click.

There are also buttons to start and stop the jiggling, toggle clicking, and pause/resume the jiggling.

## Note

This script uses the pyautogui library to move the mouse and perform clicks. Please be aware that this could interfere with your normal computer usage while the script is running. Always use this script responsibly.

## License

This project is licensed under the MIT License.
