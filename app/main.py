import sys
print("Python Path:", sys.path)

import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import WeightWiseApp

if __name__ == '__main__':
    WeightWiseApp().run()
