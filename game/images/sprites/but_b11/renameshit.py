import os
import re

# Get the current working directory (i.e. the directory of this script)
cwd = os.path.dirname(os.path.abspath(__file__))

# Iterate through all files and subfolders in the current working directory
for root, dirs, files in os.walk(cwd):
    for filename in files:
        # Check if the file is a PNG image
        if filename.endswith(".png"):
            # Extract the prefix (e.g. "b11", "a11", "b12") from the filename
            match = re.search(r'([a-z]\d+)', filename)
            if match:
                prefix = match.group(1)
                # Split the filename into parts
                parts = filename.split("_")
                
                # Check if the file matches the pattern for faces
                if not parts[-1][0].isdigit():
                    # Rename the file by changing the prefix to prefix + "_face"
                    new_filename = filename.replace(prefix, f"{prefix}_face")
                    print(f"Attempting to rename {os.path.join(root, filename)} to {os.path.join(root, new_filename)}")
                    os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                    print(f"Renamed {os.path.join(root, filename)} to {os.path.join(root, new_filename)}")
                # Check if the file matches the pattern for mouths
                elif parts[-1][0].isdigit():
                    # Rename the file by changing the prefix to prefix + "_mouth"
                    new_filename = filename.replace(prefix, f"{prefix}_mouth")
                    print(f"Attempting to rename {os.path.join(root, filename)} to {os.path.join(root, new_filename)}")
                    os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                    print(f"Renamed {os.path.join(root, filename)} to {os.path.join(root, new_filename)}")







