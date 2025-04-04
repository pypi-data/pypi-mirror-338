# slim_common_robot/test_data/__init__.py
import json
import os
import sys

# Determine which import to use based on Python version
if sys.version_info >= (3, 9):
    # Modern approach for Python 3.9+
    from importlib.resources import files
    
    def _load_json(filename):
        json_path = files("slim_common_robot.test_data").joinpath(filename)
        with json_path.open("r", encoding="utf-8") as f:
            return json.load(f)
            
elif sys.version_info >= (3, 7):
    # Python 3.7-3.8 approach
    from importlib import resources
    
    def _load_json(filename):
        with resources.open_text("slim_common_robot.test_data", filename) as f:
            return json.load(f)
else:
    # Fallback for older Python versions
    def _load_json(filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, filename), 'r', encoding="utf-8") as f:
            return json.load(f)

# Load JSON files
try:
    slim_groundplex = _load_json("slim_groundplex.json")
    triggered = _load_json("triggered.json")
except Exception as e:
    # Provide informative error if files can't be loaded
    print(f"Error loading JSON files: {e}")
    # Initialize with empty dictionaries as fallback
    slim_groundplex = {}
    triggered = {}

# Add functions to load files on demand (useful if files are large)
def load_groundplex():
    return _load_json("slim_groundplex.json")

def load_triggered():
    return _load_json("triggered.json")

# Expose both variables and functions
__all__ = ['slim_groundplex', 'triggered', 'load_groundplex', 'load_triggered']