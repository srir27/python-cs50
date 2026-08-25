import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        val = [(row['name'], row['house']) for row in reader]
        # print(val)

    with open(sys.argv[2], "w", newline="") as newfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in val:
            name = i[0]
            house = i[1]
            last, first = name.split(", ")
            row = {"first": first, "last": last, "house":house}
            writer.writerow(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
    