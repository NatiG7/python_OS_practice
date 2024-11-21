import os

# 7. Process Management

    # Objective: Work with process-related functions in os.

    # Print the Process ID (PID) of the current script.
    # Launch a new Python process to print "Hello from another process."
    # Wait for the new process to finish and print a confirmation.
    # Run a Simple Command (spawn process)
    # Long-Running Process and Monitoring
    # Handle Process Exceptions
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

# Step 4: Run a simple command
# Now, we'll use subprocess.run() to execute a simple command
# (e.g., dir or ls).

try:
    # On linux
    # result = subprocess.run(['ls'],check=True, text=True, capture_output=True)
    # On windows
    result = subprocess.run(['dir'],shell=True,check=True,capture_output=True,text=True)
    print(f"Command output:\n{result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Error running command : {e}")

# Step 5: Long-running and monitoring
# Next, we use subprocess.Popen() to run a long-running process
# (like sleep or timeout) and monitor its output.

import time

try:
    # On linux
    # process = subprocess.Popen(['sleep','5'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    # On windows
    # 5 second timeout
    # redirection to nul to avoid default windows timeout msg.
    
    process = subprocess.Popen(['timeout','5', '>nul'],stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    print("Process started, waiting for it to finish...\n")
    
    while process.poll() is None:
        print("Process running. . .")
        time.sleep(1) # Wait 1 second
        
    stdout, stderr = process.communicate() # capture remaining output
    print("\nProcess has finished.")
    if stdout:
        print(f"Output:\n\t{stdout.decode().strip()}")
    if stderr:
        print(f"Error:\n\t{stderr.decode().strip()}")
except Exception as e:
    print(f"Error occurred : {e}")
    

# Step 6: Handling exceptions

try:
    result = subprocess.run(['nonexistent_command'], check=True, text=True, capture_output=True,shell=True)
except subprocess.CalledProcessError as e:
    print(f"Process failed with error: {e}")
    print(f"Command: {e.cmd}")
    print(f"Return Code: {e.returncode}")
    print(f"Output: {e.output}")
    print(f"Error Output: {e.stderr}")