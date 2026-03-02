import subprocess
import sys
from pathlib import Path
import os
import traceback

#python -m  PyInstaller path/to/your/python/script.py
#python -m  PyInstaller C:\Users\sje8wy\Documents\Untitled-1.py

#!/usr/bin/env python3

# Set program paths here (example: multiple candidate locations)
program_paths = [
    Path(r"C:\Users\sje8wy\AppData\Local\Programs\Microsoft VS Code\Code.exe"),  # visualstudio code.exe
    Path(r"C:\Program Files\Mozilla Firefox\firefox.exe"),  # firefox.exe
    Path(r"C:\Users\sje8wy\Downloads\pomotroid-0.13.0-portable.exe"),  # pomodoro timer.exe
]
#if pomotroid.exe is the first path, the others dont run because idk

#bug 2 25 2026 pomotroid.exe runs but the others dont
#debug:
#Selected program: C:\Users\sje8wy\Downloads\pomotroid-0.13.0-portable.exe
#fixbug 2 25 25 the logic is not inside the for loop, so it does the first path and skips the rest
#Exists: True
#Is file: True
debug = False
def main():
    # Select the first existing program path from the candidates
    program_path = None
    for p in program_paths:
        if p.exists():
            program_path = p
            # Diagnostic output
            if debug:
                print("Selected program:", program_path)
                print("Exists:", program_path.exists())
                print("Is file:", program_path.is_file())
            try:
                # Forward any command-line args to the program
                proc = subprocess.run([str(program_path)] + sys.argv[1:])
                # Don't sys.exit here if you want to continue launching others
            except Exception as e:
                print("Failed to launch via subprocess.run:")
                traceback.print_exc()
                # On Windows, try os.startfile as a fallback (uses file associations)
                if os.name == "nt":
                    try:
                        print("Trying os.startfile fallback...")
                        os.startfile(str(program_path))
                        print("os.startfile succeeded (app may run detached).")
                    except Exception:
                        print("os.startfile fallback failed:")
                        traceback.print_exc()
                print("All launch attempts failed.")
    if program_path is None:
        tried = ", ".join(str(p) for p in program_paths)
        print(f"Error: none of the program paths exist. Tried: {tried}")
        sys.exit(1)
   

if __name__ == "__main__":
    main()