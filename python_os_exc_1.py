import os

# 1. Current Working Directory

    # Objective: Practice retrieving and changing the working directory.
    # Write a script to print the current working directory.
    # Change the working directory to the parent directory and print the new working directory.


# From documentation :
    # os.getcwd()
    
    # Return a string representing the current working directory.

print("\nExc 1: Print the current working directory, completed with os.getcwd() command\n")
print(f"Current working directory: {os.getcwd()}\n")
print("Exc 2:Change the working directory to the parent directory and print the new working directory.\n")

# From documentation:
    # os.fchdir(fd)

    # Change the current working directory to the directory represented by the file descriptor fd.
    # The descriptor must refer to an opened directory,not an open file.
    # As of Python 3.3, this is equivalent to os.chdir(fd).
    
os.chdir("../")
print("Directory changed with os.chdir\n")
print(f"Current working directory: {os.getcwd()}\n")