import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

try:
    input_file = sys.argv[1]
    with open(input_file) as file:
        count = 0
        for line in file:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            else:
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")