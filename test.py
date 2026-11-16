import os

path = "class1"
for filepath, folders, files in os.walk(path):
    print(filepath, folders, files)
