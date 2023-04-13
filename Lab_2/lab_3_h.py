from lab_3.Utils import linkValidation

def isFromPoland(line):
    split1 = line.split('-')
    split2 = split1[0].strip()
    return (split2.endswith(".pl"))

def findLinesPoland():
    filteredData = []
    while True:
        try:
            line = input()
            if (linkValidation(line) and isFromPoland(line)):
                filteredData.append(line)
        except EOFError:
            break
    return filteredData

def printFilteredLinesPoland():
    filteredData = findLinesPoland()
    for data in filteredData:
        print(data)

if __name__ == "__main__":
    printFilteredLinesPoland()