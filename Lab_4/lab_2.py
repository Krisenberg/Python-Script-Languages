import os
from os import environ
import shutil
import sys

def catalogs_path():
    list = []
    pathList = environ['PATH'].split(os.pathsep)
    for path in pathList:
        if(os.path.isdir(path)):
            list.append(path)
    return list

def exes_path():
    catalogs = catalogs_path()
    exes = []
    for path in catalogs:
        files = os.listdir(path)
        local_exes=[]
        for file in files:
            if(shutil.which(file) != None):
                local_exes.append(file)
        exes.append(local_exes)       
    return (catalogs, exes)

def print_output(args):
    if (len(args)<2):
        raise ValueError("Parameters are needed")
    if (args[1]=="-1"):
        print("List of all directories in the PATH environment variable:")
        dirList = catalogs_path()
        for dir in dirList:
            print(dir)
        print()
    elif (args[1]!="-0"):
        raise ValueError("Invalid parameter")
    if (args[2]=="-1"):
        print("List of all executable files in the PATH environment variable:")
        (catalogs, exes) = exes_path()
        for i in range(len(catalogs)):
            print(f"{catalogs[i]}: {exes[i]}\n")
    elif (args[2]!="-0"):
        raise ValueError("Invalid parameter")
    
            
if __name__ == '__main__':
    try:
        print_output(sys.argv)
    except ValueError as e:
        print(str(e))