# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['MouseJiggle.py'],
    pathex=['C:\\Users\\marlo.mayberry\\OneDrive - epeslogistics.com\\Documents\\Python Scripts\\Jiggle'],
    binaries=[],
    datas=[
        ('MouseJigglerLogo.png', '.'),
        ('MouseJigglerLogo2.png', '.'),
        ('MouseFavicon.ico', '.')
    ],
    hiddenimports=['pyautogui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MouseJiggle',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False if you don't want the console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='MouseFavicon.ico'  # Specify the icon file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MouseJiggle',
)
