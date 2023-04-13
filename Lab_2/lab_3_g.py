from lab_3.Utils import getDate, linkValidation

def findLinesFriday():
    filteredData = []
    while True:
        try:
            line = input()
            if linkValidation(line):
                date = getDate(line)
                if ((not date == -1) and date.weekday() == 4):
                    filteredData.append(line)
        except EOFError:
            break
    return filteredData

def printFilteredLinesFriday():
    filteredData = findLinesFriday()
    for data in filteredData:
        print(data)

if __name__ == "__main__":
    printFilteredLinesFriday()