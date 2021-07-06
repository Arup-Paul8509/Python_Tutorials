'''
open()
    This function is used to open a file.
    
    Syntax : open(filename,mode)
    Modes :
        "r"-Read
        "a"-Append
        "w"-Write
        "x"-Create
    "t"- Text mode(default)
    "b"-Binary mode

    Example: f=open("demo.txt") or f=open("demo.txt","rt")

read()
    This function is used to read the content of file.

    Example :
    f=open("demo.txt","rt")
    print(f.read())
    print(f.read(5))#returns 5 characters from the file

readline()
    This function is used to read 1 line from a file.

    Example :
    f=open("demo.txt","rt")
    print(f.readline())

close()
    This function is used to close a file
    
    Example :
    f=open("demo.txt","rt")
    print(f.read())
    f.close()

write()
    This function is used to write(using "w" mode) or append(using "a" mode) in the file.

    Example :
    f=open("demo.txt","rt")
    f.write("Hello")

    "x","a","w" will create new file if the given file doesn't exist

delete a file
    import os 
    os.remove("demo.txt")

    #check if file exists
    import os 
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")

delete folder
    import os
    os.rmdir("myfolder")
'''