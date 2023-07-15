import os

def ct():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def get_path():
    path = os.getcwd()
    
    return path

