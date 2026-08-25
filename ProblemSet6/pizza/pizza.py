import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        table = tabulate(reader, headers="firstrow", tablefmt="grid")
        print(table)
except FileNotFoundError:
    sys.exit("File does not exist")




