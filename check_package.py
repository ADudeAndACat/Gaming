"""
Script to verify if the Gaming package can be imported.
"""
import sys
import os

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
print(f"Added {current_dir} to sys.path")

try:
    print("Attempting to import Gaming package...")
    import Gaming
    print(f"Success! Gaming package found at: {Gaming.__file__}")
    
    # Try to import a specific module from Gaming
    print("Attempting to import a module from Gaming...")
    from Gaming import diceroller
    print("Successfully imported diceroller module")
    
except ImportError as e:
    print(f"Error importing Gaming package: {e}")
    print("\nDebugging information:")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    print("\nContents of current directory:")
    for item in os.listdir(current_dir):
        print(f" - {item}")
    
    print("\nIs __init__.py in the current directory?")
    if "__init__.py" in os.listdir(current_dir):
        print("Yes, __init__.py exists")
        with open(os.path.join(current_dir, "__init__.py"), "r") as f:
            print(f"Contents of __init__.py:\n{f.read()}")
    else:
        print("No, __init__.py does not exist")
