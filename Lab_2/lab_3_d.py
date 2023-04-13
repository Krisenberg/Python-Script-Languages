from lab_3.Utils import getPath, linkValidation

def suffixChecker(path):
    acceptable_suffixes = {".gif", ".jpg", ".jpeg", ".xbm"}
    for suffix in acceptable_suffixes:
        if path.endswith(suffix):
            return True
    return False

def grpahicsDownloads():
    numberOfGraphicsDownloads = 0
    numberOfOtherDownloads = 0

    while True:
        try:
            line = input()
            if linkValidation(line):
                path = getPath(line)
                if (suffixChecker(path)):
                    numberOfGraphicsDownloads += 1
                else:
                    numberOfOtherDownloads += 1
        except EOFError:
            break
    return numberOfGraphicsDownloads, numberOfOtherDownloads

def printRatio():
    numberOfGraphicsDownloads, numberOfOtherDownloads = grpahicsDownloads()
    ratio = numberOfGraphicsDownloads / numberOfOtherDownloads
    print(f'Number of graphic files downloads: {numberOfGraphicsDownloads},') 
    print(f'Number of other files downloads: {numberOfOtherDownloads},')
    print(f'Ratio is: {ratio:.2f}')

if __name__ == '__main__':
    printRatio()