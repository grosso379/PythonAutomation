import os
import re
import shutil


def getPath():
    path = input(
        r"PLease press enter for default folder, otherwise input the path of the project folder: ")
    if path == '':
        path = 'C:\\Users\\Usuario\\myProjects'
    return path


def change_directory(path):
    os.chdir(path)


def create_directory(name):
    os.mkdir(name)


def create_files():
    # styles
    os.mkdir('styles')
    style = open("./styles/style.scss", "x")
    style.close()
    # javaScript
    os.mkdir('js')
    js = open("./js/main.js", "x")
    js.close()
    # HTML
    index = open("index.html", "x")
    index.close()


if __name__ == "__main__":
    # Get current working directory
    originalPath = os.getcwd()
    # Get path for the project and name
    path = getPath()
    projectName = input("Please input the name for the new project: ")
    # Move to the project path and create project
    change_directory(path)
    create_directory(projectName)
    # Move to project and create project files
    change_directory(path + '\\' + projectName)
    create_files()
    # Return to original working directory
    os.chdir(originalPath)
