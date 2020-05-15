import os
import re
import shutil

def change_directory(path):
    os.chdir(path)

def get_content():
    content = os.listdir()
    return content

def get_extention(filename):
    root, ext = os.path.splitext
    return root, ext

if __name__ == "__main__":
    #Get path of directory to sort
    path = input(r'Input path of the folder you want to sort: ')
    #Move to that directoy
    change_directory(path)
    #Get list of files in the folder
    content = get_content()
    #Sort
    for file in content:
        root, ext = os.path.splitext(file)
        if not ext and root.endswith('Folder'):
            continue
        elif not ext:
            if not os.path.exists('DirFolder'):
                os.mkdir('DirFolder')
            shutil.move(file, r'DirFolder\\' + file)
        else:
            if not os.path.exists(ext.upper() + 'Folder'):
                os.mkdir(ext.upper() + 'Folder')
            shutil.move(file,  ext.upper() + 'Folder' + r'\\' + file)


