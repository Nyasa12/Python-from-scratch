import os

# Function to print directory contents
def print_directory_contents(path='/'):
    try:
        entries = os.listdir(path)  # Get list of files and directories
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print(f"Error: {e}")

# Run the function (default is current directory)
if __name__ == "__main__":
    print_directory_contents()

