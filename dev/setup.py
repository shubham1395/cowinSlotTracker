from cx_Freeze import setup, Executable

includefiles = ['images']
base = "Win32GUI"

setup(name="CowinSlotTracker",
      version="1.0",
      description="An application to track vacant vaccination slots.",
      executables=[Executable("CowinSlotTracker.py", base=base)],
      options={'build_exe': {'include_files':includefiles}})