from lab_3.Utils import getDataSize, linkValidation
import math

def sumDataSize():
    sum = 0

    while True:
        try:
            line = input()
            if linkValidation(line):
                dataSize = getDataSize(line)
                sum += dataSize
        except EOFError:
            break
    return float(sum/math.pow(1024, 3))

def printSumData():
    print(f'{sumDataSize():.2f} GB')

if __name__ == '__main__':
    printSumData()