import os

# 8. Advanced: Path Handling

    # Objective: Practice working with paths and navigating file structures.

    # Write a script to find the absolute path of a file named file1.txt in the current directory.
    # Check whether this path is a file or a directory.
    # Split the absolute path into its components (e.g., drive, folders, file).
    

# Step 1: finding absolute path using os.path.abspath(file)
print() # newline

file_name_to_check = './file1.txt'
absolute_path = os.path.abspath(file_name_to_check)
print('=' * 60)
print(f"Absolute path of {file_name_to_check}: {absolute_path}")
print('=' * 60)

# Step 2: Check if file or a directory
# Using the method os.path.isfile() || os.path.isdir()

if os.path.isfile(absolute_path):
    # Check if file
    print(f"{absolute_path} is a file.")

elif os.path.isdir(absolute_path):
    # Check if dir
    print(f"{absolute_path} is a directory.")

else:
    print(f"{absolute_path} does not exist.")
    

# Step 3: split the absolute path into components
# For this the method os.path.split() can be used
# The method os.path.splitdrive() separates the drive from the path.

drive, path = os.path.splitdrive(absolute_path)
folders, file =os.path.split(path)
print('=' * 60)
print("~~~ Split path result ~~~")
print(f"Drive: {drive}")
print(f"Folders: {folders}")
print(f"File: {file}")
print('=' * 60)
