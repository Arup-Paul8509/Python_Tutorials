import os
if os.path.exists("MyFolder"):
    os.rmdir("MyFolder")
    print("Folder Deleted")
else:
    print("Folder doesn't exists !")