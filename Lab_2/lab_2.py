import sys
data = ""

while True:
    try:
        line = input(sys.stdin)
        data += line + "\n"
    except EOFError:
        break
print("Data:")
print(data)