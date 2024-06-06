# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['label.py'],
    pathex=[],
    binaries=[],
    datas=[('download-1.png', '.'), ('download-2.png', '.'), ('download-3.png', '.'), ('download-4.png', '.'), ('download-5.png', '.'), ('download-6.png', '.'), ('download-7.png', '.')],
    hiddenimports=[],
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
    name='label',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='label',
)
