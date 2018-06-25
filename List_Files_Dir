# Find and list the directory and files in the given path.

# Python 3

import os

path = input("Enter the path:")

os.chdir(path)

my_dir = os.listdir()

directory = []

files = []

for content in my_dir:
    content = content.strip(" ")
    if os.path.isdir(content):
        directory.append(content)
    else:
        files.append(content)

print("Directory present in the path:\n" + ("\n").join(directory))
print()
print("Files present in the path:\n" + ("\n").join(files))
