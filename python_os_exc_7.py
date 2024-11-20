import os

# 7. Process Management

    # Objective: Work with process-related functions in os.

    # Print the Process ID (PID) of the current script.
    # Launch a new Python process to print "Hello from another process."
    # Wait for the new process to finish and print a confirmation.
    
# The os module provides a function os.getpid() to get the current process ID.

print("\nExc 1: print the Process ID (pid) of the current script")
print("\tThis can be achieved using the method os.getpid()\n")

pid = os.getpid()
print(f"Current Process ID (PID): {pid}")

# To create a new process, we can use the subprocess module.
# In this case, we will launch a new Python process
# that runs a script to print "Hello from another process."

import subprocess

# Step 2: Launch a new Python process to print "Hello from another process."
# Using subprocess to run a Python script (in this case inline)
try:
    process = subprocess.Popen(['python', '-c', 'print("\\nHello from another process")'])
    print(f"Started a new process with PID: {process.pid}")
except Exception as e:
    print(f"Error launching process: {e}")
    
# Step 3: Wait for the new process to finish and print a confirmation.

process.wait()  # Waits for the process to complete
print("The new process has finished.")