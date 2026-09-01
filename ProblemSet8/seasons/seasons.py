from datetime import date
import re
import inflect
import sys

def main():
    dob = input("Date of Birth: ")
    minutes = date_mins(dob)
    print(num_to_words(minutes))

def date_mins(dob):
    pattern = re.fullmatch(r"\d{4}-\d{2}-\d{2}", dob)
    if not pattern:
        sys.exit("Invalid date")

    try:
        date_object = date.fromisoformat(dob)
    except:
        sys.exit("Invalid date")

    if date_object > date.today():
        sys.exit("Invalid date")

    date_difference = date.today() - date_object
    minutes = date_difference.days * 24 * 60
    return minutes

def num_to_words(minutes):
    p = inflect.engine()
    in_words = p.number_to_words(minutes, andword="")
    in_words = in_words.capitalize() + " minutes"
    return in_words

if __name__ == "__main__":
    main()
