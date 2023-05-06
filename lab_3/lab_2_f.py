import re, sys, datetime

def get_entires_by_extension(tupleList, extension):
    pattern = r'^(/.*)\sHTTP/.*$'
    returnList = []
    for log in tupleList:
        match = re.match(pattern, log[3])
        if match:
            path = match.group(1)
            if path.endswith(extension):
                returnList.append(log)
    return returnList

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    extension = sys.argv[1]
    tuplesWithExtension = get_entires_by_extension(tupleList,extension)
    for line in tuplesWithExtension:
        print(line)