import sys, os
from cx_Freeze import setup, Executable

build_options = {
    "excludes": [],
    "zip_include_packages": [],
    "include_files": ["palworld_pal_edit/resources/", "pals/"],
    "zip_includes": ["palworld_pal_edit/resources/", "pals/"],
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name = "PalEdit v0.6.6",
    version = "0.6.6",
    description = "A simple tool for editing PalWorld saves",
    options={"build_exe": build_options},
    executables=[Executable("PalEdit.py", base=base, icon="palworld_pal_edit/resources/MossandaIcon.ico")],
)
