import sys
from lab_3.Utils import linkValidation
    
def countIncorrectLines():
    incorrectLinesNumber = 0
    totalNumber = 0

    while True:
        try:
            link = input()
            totalNumber += 1
            if (not linkValidation(link)):
                incorrectLinesNumber += 1
        except EOFError:
            break
    return incorrectLinesNumber, totalNumber

def printIncorrectLinesNumber():
    x,y = countIncorrectLines()
    percentage = (x/y)*100
    print(f'{percentage}%')

if __name__ == '__main__':
    printIncorrectLinesNumber()