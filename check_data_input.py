import os

folder = "data_input"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' was not found, so it has been created.")
    print("í±‰ Please add .txt files into the 'data_input' folder.")
else:
    print(f"Folder '{folder}' already exists.")
