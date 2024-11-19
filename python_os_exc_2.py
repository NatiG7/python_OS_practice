import os

# 2. List Files and Directories

# Objective: Understand how to work with directories and their contents.

    # Write a script that lists all files and directories in the current directory.
    # Filter and print only files with the .txt extension.
    # Create a list of all subdirectories and save their names into a new .txt file named subdirectories.txt.
    
folder = '.'

print("\nExc 1 : List all files and directories in the current dir. Completed with os.listdir({PATH})")
print(f"\n\t Current directory : {os.getcwd()}")
print(f"\n\t All files in the current directory : {os.listdir(folder)}")

print("\nExc 2 : filter and print only files with the .txt extension")
print("\nCompleted by setting the list inside a variable and filtering using file.endswith()")
#files and directories in the folder
files_and_dirs = os.listdir(folder)
#filter only text files
text_files = [file for file in files_and_dirs if file.endswith('.txt')]
print(f"\n\tText files only from current directory : {text_files}")

print("\nExc 3: create a list of all subdirs and save them to a new txt named subdirectories.txt")
print("\nCompleted by using the method os.path.isdir()\niterating over our files_and_dirs list that we got with listdir")
#Get all sub-dirs
subdirs = [dir for dir in files_and_dirs if os.path.isdir(dir)]
#Print the list of sub-dirs
print(f"\n\tSub directories :{subdirs}")

# Save the list of subdirectories to a new .txt file
with open('subdirectories.txt', 'w') as file:
    for subdir in subdirs:
        file.write(subdir + '\n')

print("\nSubdirectories have been saved to 'subdirectories.txt'.")