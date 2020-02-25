import os

def listFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + listFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles