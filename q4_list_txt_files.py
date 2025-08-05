import os

txt_files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]

print("Text files in current directory:")
for file in txt_files:
    print(file)
