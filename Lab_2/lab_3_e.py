from lab_3.Utils import getCode, linkValidation


def findLinesCode200():
    filteredData = []
    while True:
        try:
            line = input()
            if linkValidation(line):
                code = getCode(line)
                if (code == 200):
                    filteredData.append(line)
        except EOFError:
            break
    return filteredData

def printFilteredLinesCode200():
    filteredData = findLinesCode200()
    for data in filteredData:
        print(data)

if __name__ == "__main__":
    printFilteredLinesCode200()