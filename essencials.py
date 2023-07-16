import os

# Function to clear the console
def ct():
    # Check the operating system and execute the appropriate command to clear the console
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

# Function to get the current path
def get_path():
    # Get the current working directory path
    path = os.getcwd()

    return path

# Function to check if a file exists in the current directory and delete it if it does
def del_file(filename):
    # Check if the specified filename exists in the directory
    if os.path.exists(filename):
        # Delete the file using the appropriate command based on the operating system
        os.remove(filename)

def start_py_file(file):
    os.system(f'python {file}')