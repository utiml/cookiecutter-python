import subprocess


# Git
try:
    print("Initializing git repository...")
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Initial commit"])
    print("Created initial commit.")
except Exception as e:
    print("Error when initializing git: " + e)

# Setup
try:
    print("Setting up environment...")
    subprocess.call(["make", "setup"])
    print("Environment setup.")
except Exception as e:
    print("Error when setting up environment: " + e)

# lint
try:
    print("Setting up environment...")
    subprocess.call(["make", "lint"])
    print("Environment setup.")
except Exception as e:
    print("Error when setting up environment: " + e)

# coverage
try:
    print("Setting up environment...")
    subprocess.call(["make", "coverage"])
    print("Environment setup.")
except Exception as e:
    print("Error when setting up environment: " + e)
