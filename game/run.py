import sys
import os

# Add 'src' to sys.path so modules like 'youtube' can be imported directly
src_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

if __name__ == '__main__':
    # Import main from the src folder
    import main
