import os

# 5. Environment Variables

    # Objective: Learn how to access and modify environment variables.

    # Print the value of the PATH environment variable.
    # Add a new environment variable named MY_VARIABLE with the value PythonOS.
    # Retrieve and print the value of MY_VARIABLE.


print("Exc 1: Print the value of the PATH environment variable")
print("\n\tThis can be done by accessing the os.environ method")
print("\n\twhile referencing ['PATH'], no bracket call will print all vars.\n\nPrinting PATH\n")
print("*" * 60)
print(os.environ['PATH'])
print("*" * 60 +"\n")

print("Exc 2: Add a new environment variable name MY_VARIABLE with the value PythonOS\n")
print("\n\tThis is done using the os.environ[] assignment\n\tE.g : os.environ['MY_VARIABLE'] = 'PythonOS'\n")
os.environ['MY_VARIABLE'] = 'PythonOS'
print("$--Environment variable MY_VARIABLE added.")

print("Exc 3: Retrieve and print the value of MY_VARIABLE")
print("\n\tAccessing the newly created variable using os.environ['MY_VARIABLE']\n")
print(f"MY_VARIABLE = {os.environ['MY_VARIABLE']}")


# os.environ behaves like a dictionary. You can iterate through it to view all environment variables:
for key, value in os.environ.items():
    print(f"{key} = {value}")
