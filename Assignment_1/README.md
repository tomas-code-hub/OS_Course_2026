# Assignment 1: Environment Setup & Basic System Info

**Objective:** Get comfortable with the development environment (Ubuntu 24.04), version control, and basic OS-level commands.  
**Status:** Completed  
**Source Code:** `system_info.py`  

---

## Report & Justification

For this initial setup, I wrote a Python script utilizing standard built-in libraries to interact with the system environment and retrieve metadata. Here is the breakdown of the modules used:

*   **`platform.system()` & `platform.release()`:** I used the `platform` module because it is the most reliable cross-platform way to extract the OS name (Linux) and the specific Kernel version running underneath the Ubuntu environment.
*   **`getpass.getuser()`:** This function safely queries the environment variables (like `$USER` or `$LOGNAME`) to accurately retrieve the currently logged-in user without needing elevated privileges.
*   **`os.getcwd()`:** This method interfaces directly with the OS to dynamically fetch the Current Working Directory path, which is crucial for verifying where processes are being executed.

## Proof of Execution

Below is the console output demonstrating the script successfully fetching the OS, Kernel, User, and Directory information:

![alt text](image.png)