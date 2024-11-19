import os

#3. File Creation and Removal

# Objective: Practice file creation and deletion using os.
    # Write a script to create 5 empty files named file1.txt to file5.txt in the current directory.
    # Delete file3.txt and file4.txt.
    # Check if a file named file5.txt exists. If it does, rename it to file5_renamed.txt.

print("\nExc 1: Write a script to create empty text files named file1 to file5\n")
print("\tThis can be accomplished using the method open()\n\tin mode 'w' for creating new files\n")

for i in range(1,6):
    with open(f'file{i}.txt','w') as f:
        print(f"Creating file : file{i}.txt")
        pass # open close for empty files.
    
files_and_dirs = os.listdir()
print("\nExc 2: Delete file3.txt and file4.txt")
print("\n\tFor this exercise use os.remove()")
print(f"\nCurrent files : {files_and_dirs}\n")
print("\n\tRunning os.remove() on file3 and file4")

if os.path.exists("file3.txt"):
    os.remove("file3.txt")
if os.path.exists("file4.txt"):
    os.remove("file4.txt")

# After os.{action}, methods such as listdir need to be run again
# to fetch updated directory/file contents.

files_and_dirs = os.listdir()
print(f"\nAfter removal: \n---> Current files : {files_and_dirs}\n")

print("Exc 3: Check if a file named file5.txt exists\n\tIf it does, rename it to file5_renamed.txt")
print("\n\t For this use os.path.exists and os.rename")

if os.path.exists('file5.txt'):
    os.rename('file5.txt', 'file5_renamed.txt')
    print("\nfile5.txt renamed.")
    
files_and_dirs = os.listdir()
print(f"After renaming : \n---> Current files : {files_and_dirs}")