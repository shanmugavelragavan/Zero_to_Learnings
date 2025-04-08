# Delete a File in Python

# 1. Removing the files or a single file from a particular directory when it is no longer required is the basic concept of deleting a file. To delete a file, you must import the module os, then use the remove() function provided by the module to delete the file. It takes the file location as a parameter.
#     Syntax:
#          os.remove ( file_location )

# 2. This is a code snippet that demonstrates how to delete a file in Python. The code imports the "os" module, which provides a way to interact with the operating system. The code then checks if the specified file "data.txt" exists using the "os.path.exists()" method. If the file exists, it is deleted using the "os.remove()" method. If the file does not exist, a message "File Not Found" is printed. The "os.remove()" method raises an exception if the file is not found, so it is a good practice to check if the file exists before trying to delete it.



import os

if os.path.exists("vel.txt"):
    os.remove("vel.txt")
    #os.rmdir("folder name")
else:
    print("File not Found")