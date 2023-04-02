import subprocess
from subprocess import run, PIPE, Popen
from pathlib import Path
from collections import Counter
import sys
import csv

def runner(path):
    if path.exists():
        if path.is_dir():
            textFiles = list(path.glob("*.txt"))
            process = Popen(r"C:\Users\Kris\Documents\Studia\Semestr_IV\Jezyki_skryptowe_L\Laboratoria\Lab_4\FileAnalyzer\Debug\FileAnalyzer.exe", stdin=PIPE, stdout=PIPE, text=True)
            for file in textFiles:
                currentPath = path
                #result = run([r"C:\Users\Kris\Documents\Studia\Semestr_IV\Jezyki_skryptowe_L\Laboratoria\Lab_4\FileAnalyzer\Debug\FileAnalyzer.exe"],stdin=str(path.joinpath(file)),stdout=PIPE,text=True)
                process.stdin.write(str(currentPath.joinpath(file))+'\n')
            process.stdin.close()
            fieldnames = ['path', 'charNo', 'wordNo', 'linesNo', 'mfChar', 'mfWord']
            outputDictList = [row for row in csv.DictReader(process.stdout.readlines(), fieldnames=fieldnames)]
            return outputDictList
        else:
            raise Exception("It is not a valid directory path")
    else:
        raise Exception("This file/directory doesn't exist")
    
        
def summarizer(dictList):
    sumCharNumbers = [int(dict['charNo']) for dict in dictList]
    sumWordNumbers = [int(dict['wordNo']) for dict in dictList]
    sumLinesNumbers = [int(dict['linesNo']) for dict in dictList]
    counter = Counter(dict['mfChar'] for dict in dictList)
    mcChar = counter.most_common(1)[0][0]
    counter = Counter(dict['mfWord'] for dict in dictList)
    mcWord = counter.most_common(1)[0][0]
    return (str(len(dictList)), str(sum(sumCharNumbers)), str(sum(sumWordNumbers)), str(sum(sumLinesNumbers)), mcChar, mcWord)


def printer(summarizedTuple):
    print("\nNumber of analyzed files: " + summarizedTuple[0])
    print("Total number of characters: " + summarizedTuple[1])
    print("Total number of words: " + summarizedTuple[2])
    print("Total number of lines: " + summarizedTuple[3])
    print("Most common character: " + summarizedTuple[4])
    print("Most common word: " + summarizedTuple[5])



if __name__ == "__main__":
    dirPath = sys.argv[1]
    #printer(summarizer(runner(Path(dirPath))))
    try:
        printer(summarizer(runner(Path(dirPath))))
    except IndexError:
        print("Index error - check if the directory and files aren't empty")
    except Exception as e:
        print(str(e))