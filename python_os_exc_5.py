import os

# 5. Environment Variables

    # Objective: Learn how to access and modify environment variables.

    # Print the value of the PATH environment variable.
    # Add a new environment variable named MY_VARIABLE with the value PythonOS.
    # Retrieve and print the value of MY_VARIABLE.


print("Exc 1: Print the value of the PATH environment variable")
print("\n\tThis can be done by accessing the os.environ method")
print("\n\twhile referencing ['PATH'], no bracket call will print all vars.\nPrinting PATH\n")
print("*" * 60)
print(os.environ['PATH'])
print("*" * 60 +"\n")

print("Exc 2: Add a new environment variable name MY_VARIABLE with the value PythonOS\n")
print("\n\tThis is done using the os.environ[] assignment")