import os

folder = "data_input"

# Step 1: Check if data_input folder exists
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' was not found, so it has been created.")
    print("Ì±â Please add .txt files into the 'data_input' folder.")
else:
    print(f"Folder '{folder}' exists. Reading .txt files...\n")

    # Step 2: List all .txt files
    txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]

    if not txt_files:
        print("‚ùó No .txt files found in data_input.")
    else:
        for file in txt_files:
            file_path = os.path.join(folder, file)
            print(f"--- {file} ---")
            with open(file_path, 'r') as f:
                content = f.read()
                print(content)
                print()
