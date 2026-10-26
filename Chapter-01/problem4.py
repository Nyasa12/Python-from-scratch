import os

def print_directory_contents(path='.'):
    try:
        entries = os.listdir(path)  
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_directory_contents()
    