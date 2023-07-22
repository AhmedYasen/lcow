import os
import sys

def touch(file_path):
    if os.path.exists(file_path):
        # If the file exists, update its access and modification timestamps
        os.utime(file_path, None)
    else:
        # If the file does not exist, create a new empty file
        with open(file_path, 'a'):
            os.utime(file_path, None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python touch.py <file_path>")
    else:
        file_path = sys.argv[1]
        touch(file_path)
