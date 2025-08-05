import os

path = input("Enter path to check: ")

if os.path.isfile(path):
    print(f"{path} is a file.")
elif os.path.isdir(path):
    print(f"{path} is a directory.")
else:
    print(f"{path} is neither a file nor a directory.")
