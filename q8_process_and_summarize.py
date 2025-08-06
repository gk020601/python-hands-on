import os

input_folder = "data_input"
output_folder = "data_output"
summary_path = os.path.join(output_folder, "summary.txt")

# Step 1: Ensure data_input folder exists
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print(f"Created '{input_folder}'. Please add .txt files to process.")
    exit()

# Step 2: Create data_output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Step 3

Prepare summary file
summary_lines = ["Filename | Line Count | Word Count\n", "-"*40 + "\n"]

# Step 4: Process .txt files
txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

if not txt_files:
    print("â— No .txt files found in data_input.")
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
                continue
            line_count += 1
            word_count += len(line.split())
            processed_lines.append(line.replace("temp", "permanent"))

        # Save processed file
        with open(output_path, 'w') as f:
            f.writelines(processed_lines)

        # Add to summary
        summary_lines.append(f"{file} | {line_count} | {word_count}\n")
        print(f"âœ… {file}: {line_count} lines, {word_count} words â†’ saved")

    # Save summary file
    with open(summary_path, 'w') as f:
        f.writelines(summary_lines)

    print(f"\ní³„ Summary saved to {summary_path}")
