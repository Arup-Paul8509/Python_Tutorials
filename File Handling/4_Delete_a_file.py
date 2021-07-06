import os
if os.path.exists("Trial.txt"):
    os.remove("Trial.txt")
    print("File Deleted")
else:
    print("File doesn't exists!")