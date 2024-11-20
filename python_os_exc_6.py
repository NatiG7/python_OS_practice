import os

# 6. File and Directory Permissions

    # Objective: Work with file and directory permissions.

    # Write a script to check the permissions of a file (subdirectories.txt created earlier).
    # Modify the permissions to make the file read-only.
    # Verify the change and handle an exception if the file cannot be modified afterward.
    
file_to_check = './subdirectories.txt'

# Check if the file exists and check permissions
print("\nExc 1: Write a script to check permissions")
print("\nChecking file permissions can be achieved using os.access({file}, os.(R/W/X)_OK)\n")
if os.path.exists(file_to_check):
    print("File exists. Checking permissions :")
    print(f"\tReadable : {os.access(file_to_check,os.R_OK)} (R_OK)")
    print(f"\tWriteable : {os.access(file_to_check,os.W_OK)} (W_OK)")
    print(f"\tExecutable : {os.access(file_to_check,os.X_OK)} (X_OK)")
else:
    print(f"The file {file_to_check} does not exist.")

# Modify to read-only
# 0o444: Read-only.
# 0o666: Read and write.
# 0o777: Full permissions (read, write, execute).
print("\nExc 2: Modify the permissions to make the file read-only")
print("\n\tThis can be done using the os.chmod() method, read only in octal is 0o444")
os.chmod(file_to_check, 0o444)
print(f"Changed permissions of {file_to_check} to read-only.")

# Verify and handle the exception
print("\nExc 3: Verify changes and handle an exception if the file cannot be modified")
print("\tLets try writing to that file again")

try:
    with open(file_to_check,'w') as f:
        f.write("This should not work!")
except IOError as e:
    print(f"Error: Cannot modify the file. {e}")