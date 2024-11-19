import os

# 4. Directory Creation and Navigation

    # Objective: Work with creating and removing directories.

    #Create a directory structure:
        # project/
        #   ├── src/
        #   ├── tests/
        #   └── docs/
    # Print the tree-like structure of the project directory.
    # Remove the docs directory.
    
def makedirs(dir):
    try:
        os.makedirs(dir)
    except:
        pass
folder = "project"
sub_folders = ["src","tests","docs"]

print(f"\nFolders to be created : Main: {folder}\n\tSub-directories for creation : {sub_folders}")
print("\n\tFor this we will use os.makedirs()")
print("\tthat was implemented into makedirs(dir) function\n")

if not folder:
    os.mkdir(folder)
print(f"Created main folder : {folder}")

for folder in sub_folders:
    os.makedirs(f"./project/{folder}", exist_ok=True)
    print(f"Created folder : {folder}")


def print_tree(folder, indent=0):
    for root, dirs, files in os.walk(folder):
        level = root.replace(folder, '').count(os.sep)  # Determine the depth
        indent = ' ' * 4 * level  # 4 spaces per level of depth
        print(f"{indent}|-- {os.path.basename(root)}")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}|-- {file}")

# Test the function on the 'project' directory
print("\nTree-structure:\n")
print_tree('./project')

#os.rmdir('./project/docs')