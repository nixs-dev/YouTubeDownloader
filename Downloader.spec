# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['__init__.py', 'Controllers\\Downloader.py', 'views\\Main.py'],
             pathex=['C:\\Users\\x\\Desktop\\YouTubeDownloader', 'C:\\Windows\\System32\\downlevel'],
             binaries=[('c://python36/python36.dll', '.'), ('c://python36/vcruntime140.dll', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Downloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='icon.ico')
