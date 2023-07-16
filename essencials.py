import os

def ct():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def get_path():
    path = os.getcwd()
    
    return path

def file_exists(filename):
    path = get_path()
    files_in_path = os.listdir(path)
    
    if filename in files_in_path:
        os.system(f'del {filename}')
        pass
    else:
        pass