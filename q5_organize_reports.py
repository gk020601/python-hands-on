import os
import shutil

# Step 1: Create reports directory if it doesn't exist
reports_dir = "reports"
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Created '{reports_dir}' directory.")
else:
    print(f"'{reports_dir}' directory already exists.")

# Step 2: List all .txt files in the current directory
txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

# Step 3: Move each .txt file into the reports folder
for file in txt_files:
    print(f"Moving {file} to {reports_dir}/")
    shutil.move(file, os.path.join(reports_dir, file))
