import re

DEBUG = False

def correctPasswordCount(input):
    correct_count = 0

    for e in input:
        count = e["password"].count(e["symbol"])
        if e["min_count"] <= count and count <= e["max_count"]:
            correct_count += 1

    return correct_count

### parse input

input_file = open("input.txt", "r")
input = []

try:
    for line in input_file:
        e = re.split("-| |: |\n", line)
        input.append({"min_count":int(e[0]), "max_count":int(e[1]), "symbol":e[2], "password":e[3]})
except:
    sys.exit("An error occured while parsing the input file. Check your input.txt for correct format.\n")

if DEBUG:
    print(*input, sep = "\n")

# Output for part 1
print(correctPasswordCount(input))
