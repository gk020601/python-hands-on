import os

input_folder = "data_input"
output_folder = "data_output"

# Step 1: Ensure data_input folder exists
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print(f"Created '{input_folder}'. Please add .txt files to process.")
    exit()

# Step 2: Create data_output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Step 3: Process .txt fi


txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

if not txt_files:
    print("❗ No .txt files found in data_input.")
else:
    for file in txt_files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        with open(input_path, 'r') as f:
            lines = f.readlines()

        processed_lines = []
        word_count = 0
        line_count = 0

        for line in lines:
            if line.strip().startswith('#'):
                continue  # Skip comment lines

            line_count += 1
            word_count += len(line.split())
            modified_line = line.replace("temp", "permanent")
            processed_lines.append(modified_line)

        # Save to data_output folder
        with open(output_path, 'w') as f:
            f.writelines(processed_lines)

        print(f"✅ {file}: {line_count} lines, {word_count} words (saved to data_output)")
