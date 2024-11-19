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


# Syntax: os.chdir(path)
# path: A complete path of directory to be changed to new directory path.
# Returns: Doesn’t return any value
    
os.chdir("../")
print("Directory changed with os.chdir\n")
print(f"Current working directory: {os.getcwd()}\n")