from lab_3.Utils import getDataSize, getPath, linkValidation

def findLargestData():
    maxSize = 0
    path = ""

    while True:
        try:
            line = input()
            if linkValidation(line):
                dataSize = getDataSize(line)
                if (dataSize > maxSize):
                    maxSize = dataSize
                    path = getPath(line)
        except EOFError:
            break
    return maxSize, path

def printLargestData():
    maxSize, path = findLargestData()
    print(f'Path: {path}, largest data size: {maxSize}')

if __name__ == '__main__':
    printLargestData()