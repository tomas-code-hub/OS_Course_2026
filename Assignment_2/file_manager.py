import os
import stat
import sys

def get_permissions(file_path):
    st = os.stat(file_path)
    return stat.filemode(st.st_mode)

def list_directory_info(path):
    try:
        if not os.path.isdir(path):
            print(f"Error: {path} is not a directory.")
            return

        print(f"{'File Name':<25} | {'Size (Bytes)':<12} | {'Permissions'}")
        print("-" * 55)

        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                perms = get_permissions(full_path)
                print(f"{entry:<25} | {size:<12} | {perms}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    list_directory_info(target)