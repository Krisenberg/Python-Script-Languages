from lab_3.Utils import getHour, linkValidation
import sys


def findLinesHourBetween22And6():
    filteredData = []
    while True:
        try:
            line = input()
            if linkValidation(line):
                hour = getHour(line)
                if (hour >= 22 or (hour >= 0 and hour < 6)):
                    filteredData.append(line)
        except EOFError:
            break
    return filteredData

def printFilteredLinesHourBetween22And6():
    filteredData = findLinesHourBetween22And6()
    for data in filteredData:
        print(data)

if __name__ == "__main__":
    printFilteredLinesHourBetween22And6()