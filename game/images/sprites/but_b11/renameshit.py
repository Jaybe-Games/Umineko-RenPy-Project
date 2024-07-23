import os

# Get the current working directory (i.e. the directory of this script)
cwd = os.path.dirname(os.path.abspath(__file__))

# Iterate through all files in the current working directory
for filename in os.listdir(cwd):
    # Check if the file is a PNG image and contains 'b11'
    if filename.endswith(".png") and 'b11' in filename:
        # Split the filename into parts
        parts = filename.split("_")
        
        # Check if the file matches the pattern for faces
        if not parts[-1][0].isdigit():
            # Rename the file by changing 'b11' to 'b11face'
            new_filename = filename.replace('b11', 'b11_face')
            print(f"Attempting to rename {filename} to {new_filename}")
            os.rename(os.path.join(cwd, filename), os.path.join(cwd, new_filename))
            print(f"Renamed {filename} to {new_filename}")
        # Check if the file matches the pattern for mouths
        elif parts[-1][0].isdigit():
            # Rename the file by changing 'b11' to 'b11mouth'
            new_filename = filename.replace('b11', 'b11_mouth')
            print(f"Attempting to rename {filename} to {new_filename}")
            os.rename(os.path.join(cwd, filename), os.path.join(cwd, new_filename))
            print(f"Renamed {filename} to {new_filename}")







