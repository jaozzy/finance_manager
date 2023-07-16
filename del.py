import os
import sys
from essencials import ct

# Cleans the terminal
ct()

# Define a function to clean files with a specific extension in the current directory
def clean():
    # Get the current directory path
    path = os.getcwd()
    
    # Get the extension from command-line argument
    ext = sys.argv[1]
    
    # Get the list of files in the directory
    files = os.listdir(path)
    
    # Iterate over the files and delete the ones with the specified extension
    for file in files:
        if file.endswith(f'.{ext}'):
            os.system(f'del {file}')

# Call the 'clean' function
clean()