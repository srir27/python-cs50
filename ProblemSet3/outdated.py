months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        date = date.replace(" ", "/")
        date_parts = date.split("/")

        month_value = date_parts[0]
        days = date_parts[1]
        year = int(date_parts[2])
        
        if month_value.isalpha():
            if "," not in days:
                continue
            day = int(days.replace(",", ""))
        else:
            day = int(days)

        if month_value in months:
            month = months.index(month_value) + 1
        else:
            month = int(month_value)

        if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 1636):
            continue
        print(f"{year}-{month:02}-{day:02}")

    except(ValueError, IndexError):
        continue
    break