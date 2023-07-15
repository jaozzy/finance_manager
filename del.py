import os
import sys
from essencials import ct

ct()

def clean():
    path = os.getcwd()
    ext = sys.argv[1]
    files = os.listdir(path)
    
    for file in files:
        if file.endswith(f'.{ext}'):
            os.system(f'del {file}')

clean()