import os
import platform
import getpass

print("== System Information ==")
# Operating System name and kernel version
print(f"OS Name: {platform.system()}")
print(f"Kernel Version: {platform.release()}")

# Current logged-in user
print(f"Logged-in User: {getpass.getuser()}")

# Current working directory
print(f"Current Working Directory: {os.getcwd()}")

