import re

def main():
        print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(0?[1-9]|1[0-2])(?::([0-5]\d))? (AM|PM) to (0?[1-9]|1[0-2])(?::([0-5]\d))? (AM|PM)$"
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError
    start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm = match.groups()

    if start_minute is None:
        start_minute = "00"
    if end_minute is None:
        end_minute = "00"

    start_hour = int(start_hour)
    end_hour = int(end_hour)

    start_minute = int(start_minute)
    end_minute = int(end_minute)

    if start_minute > 59 or end_minute > 59:
        raise ValueError

    if start_ampm.upper() == "PM" and start_hour != 12:
        start_hour = start_hour + 12
    if start_ampm.upper() == "AM" and start_hour == 12:
        start_hour = 0
    if end_ampm.upper() == "PM" and end_hour != 12:
        end_hour = end_hour + 12
    if end_ampm.upper() == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

if __name__ == "__main__":
    main()