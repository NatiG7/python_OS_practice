import os
import subprocess
import time


def print_current_pid():
    """Print the Process ID (PID) of the current script."""
    pid = os.getpid()
    print(f"Current Process ID (PID): {pid}")

def launch_new_python_process():
    """Launch a new Python process to print a message."""
    try:
        process = subprocess.Popen(['python', '-c', 'print("Hello from another process")'])
        print(f"Started a new process with PID: {process.pid}")
        process.wait()  # Wait for process to complete
        print("The new process has finished.")
    except Exception as e:
        print(f"Error launching process: {e}")

def run_simple_command(command):
    """Run a simple system command using subprocess.run."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        print(f"Command output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def long_running_process_and_monitor(command, interval=1):
    """Run a long-running process and monitor its state."""
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print("Process started, monitoring its state...")
        while process.poll() is None:  # Check if the process is still running
            print("Process is running...")
            time.sleep(interval)
        stdout, stderr = process.communicate()  # Get final output/error
        print(f"Process finished with return code {process.returncode}")
        if stdout:
            print(f"Output:\n{stdout.decode().strip()}")
        if stderr:
            print(f"Error:\n{stderr.decode().strip()}")
    except Exception as e:
        print(f"Error during process monitoring: {e}")

def handle_process_exceptions(command):
    """Demonstrate handling of exceptions in subprocess.run."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Process failed with error: {e}")
        print(f"Command: {e.cmd}")
        print(f"Return Code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error Output: {e.stderr}")

# Example Debug Function
def process_debug_toolkit():
    print("=== Process Management Debug Toolkit ===")
    print_current_pid()
    print("\n--- Launching a New Python Process ---")
    launch_new_python_process()
    print("\n--- Running a Simple Command ---")
    run_simple_command('dir' if os.name == 'nt' else 'ls')
    print("\n--- Monitoring a Long-Running Process ---")
    long_running_process_and_monitor('timeout 5' if os.name == 'nt' else 'sleep 5')
    print("\n--- Handling a Failing Command ---")
    handle_process_exceptions('nonexistent_command')

# Call the Debug Toolkit
if __name__ == "__main__":
    process_debug_toolkit()
