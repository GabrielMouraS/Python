import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter", "glob", "shutil", "cv2_collage"]}

base = None
if sys.platform =="win32":
    base = "Win32GUI"

setup(
    name = "Gerador de Colagem",
    version = "0.2",
    description = "Colagem de Imagens",
    options = {"build_exe": build_exe_options},
    executables = [Executable("colagem.py", base=base)]
)