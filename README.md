<h1>Mouse Jiggler</h1>

<p><strong>Mouse Jiggler</strong> is a simple tool that prevents your system from going idle by gently moving the mouse—and optionally clicking—at configurable intervals. Built in Python, it runs as a standalone Windows .exe with no installation or admin rights required.</p>

<h2>Features</h2>
<ul>
  <li>Move the mouse cursor at configurable X and Y distances</li>
  <li>Optional clicker with configurable clicks per minute</li>
  <li>Set how long the app should run</li>
  <li>Pause/Resume during operation</li>
  <li>Shows remaining time and total time</li>
  <li>System tray integration with Start/Stop/Open/Exit controls</li>
  <li>Dark mode GUI using <code>ttkbootstrap</code></li>
</ul>

<h2>How to Use (Windows)</h2>
<ol>
  <li>Run <code>MouseJiggle.exe</code> from the <code>dist/</code> folder.</li>
  <li>Enter:
    <ul>
      <li>Run duration (in minutes)</li>
      <li>Movement distances (X and Y)</li>
      <li>Clicks per minute (optional)</li>
      <li>Start and end time window</li>
    </ul>
  </li>
  <li>Click <strong>Start</strong> to begin.</li>
  <li>Use the buttons to Pause, Resume, Stop, or toggle the clicker.</li>
</ol>

<h2>System Tray Options</h2>
<ul>
  <li><strong>Open App</strong> — Reveal the main window</li>
  <li><strong>Start (1 Hour)</strong> — Instantly begin a default 1-hour jiggle session</li>
  <li><strong>Pause/Resume</strong> — Temporarily suspend/resume activity</li>
  <li><strong>Stop</strong> — End current session</li>
  <li><strong>Quit</strong> — Fully close the app</li>
</ul>

<h2>File Structure</h2>
<pre><code>MouseJiggler/
├── dist/
│   └── MouseJiggle.exe         # Compiled .exe (Windows only)
├── MouseJigglerLogo.png        # GUI image (idle)
├── MouseJigglerLogo2.png       # GUI image (active)
├── MouseFavicon.ico            # App/system tray icon
├── MouseJiggle.py              # Python source code
├── README.md                   # This file
</code></pre>

<h2>Notes</h2>
<ul>
  <li>No installation required</li>
  <li>No changes made to system settings</li>
  <li>May be flagged by antivirus due to being unsigned</li>
</ul>

<h2>For Developers</h2>

<h3>Requirements</h3>
<ul>
  <li>Python 3.10+</li>
  <li><code>pyautogui</code></li>
  <li><code>ttkbootstrap</code></li>
  <li><code>keyboard</code>, <code>Pillow</code>, <code>pystray</code></li>
</ul>

<h3>Install dependencies</h3>
<pre><code>pip install pyautogui keyboard pillow pystray ttkbootstrap
</code></pre>

<h3>Run from source</h3>
<pre><code>python MouseJiggle.py
</code></pre>

<h3>Build .exe using PyInstaller</h3>
<pre><code>pyinstaller --onefile --windowed --icon=MouseFavicon.ico ^
--add-data "MouseFavicon.ico;." ^
--add-data "MouseJigglerLogo.png;." ^
--add-data "MouseJigglerLogo2.png;." ^
MouseJiggle.py
</code></pre>

<p><em>Note:</em> Use <code>;</code> on Windows and <code>:</code> on macOS/Linux for <code>--add-data</code>.</p>

<h2>License</h2>
<p>MIT License</p>
