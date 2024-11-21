import os
import subprocess

# Stuff to make
print("=" * 75)
directory_to_create = "Submission"
files_to_create = ['fileA.txt','fileB.txt','fileC.txt']

# Check if directory exists, if not create it

if directory_to_create:
    pass
elif not directory_to_create:
    os.mkdir(directory_to_create)

# Move to the created directory
# Create files
# Leave directory.

os.chdir(directory_to_create)
for file in files_to_create:
    with open(f'{file}','w') as f:
        print(f"Created file : {file}")
        f.write(f"This is file {file}")
        
print("=" * 75)
os.chdir('../')

# Listing all files and getting absolute path for each

# List all files
files_in_directory = os.listdir(directory_to_create)

# Iterate each and retrieve abspath.
for file in files_in_directory:
    print(f"{file} Absolute Path : {os.path.abspath(file)}")

# Split fileA abspath into componenets

# First file in dir index 0
fileA_abs_path = os.path.abspath(files_in_directory[0])

# Unpacking tuple to split into components
drive, path = os.path.splitdrive(fileA_abs_path)
folders, file = os.path.split(path)
print('=' * 75)
print("~~~ Split path result ~~~")
print(f"Drive: {drive}")
print(f"Folders: {folders}")
print(f"File: {file}")
print('=' * 75)

# Set fileA.txt to read only
fileA = './Submission/fileA.txt'
os.chmod(fileA,0o666)

# Try writing to fileA and handle exception
try:
    with open(fileA,'w') as f:
        f.write("This should not work!")
except IOError as e:
    print(f"Error: Cannot modify the file. {e}")
    
print('=' * 75)

# Print current PATH variable

path_variable = os.environ['PATH']
print(f"Current PATH variable : {path_variable}")
print('=' * 75)

# Create a new environment variable SUBMISSION_VAR with the value OS_Assignment.
os.environ['SUBMISSION_VAR'] = 'OS_Assignment'
print(f"Submission Var : {os.environ['SUBMISSION_VAR']}")

# Return the PID of this script.

this_pid = os.getpid()
print(f"Current PID : {this_pid}")

# Launch a new process to run the ls (Linux/Mac)
# or dir (Windows) command and capture its output.

try:
    new_process = subprocess.run(['dir'],shell=True,check=True,capture_output=True)
    print(f" Ran command DIR , Command output:\n\t{new_process.stdout}")
    print("=" * 75)
except subprocess.CalledProcessError as e:
    print(f"Error running command : {e}")

# Search for fileB.txt in the Submission directory.
# If found, print its absolute path.
# If not, print a message saying it wasn't found.

# The specific file
file_to_search = './Submission/fileB.txt'

if os.path.exists(file_to_search):
    print("File exists.")
    print(f"Absolute path : {os.path.abspath(file_to_search)}")
else:
    print(f"The file {file_to_search} was not found.")
