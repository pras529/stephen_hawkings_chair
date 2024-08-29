import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.hardware.facial_detection import detect_facial_movement
from src.interface.gui import run_gui

if __name__ == "__main__":
    # Start GUI and facial movement detection
    run_gui(detect_facial_movement)
