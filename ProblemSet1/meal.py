def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <=13 :
        print("lunch time")
    elif  18 <= t <= 19 :
        print("dinner time")

def convert(time):
    time = time.replace(":", " ")
    split1 = time.split()
    if len(split1) == 2:
        hours, mins = split1
        # print(split1)
        decimal_hours = int(hours) + int(mins) / 60
        return (decimal_hours)
    else:
        hours, mins, time_of_day = split1
        hours = int(hours)
        if time_of_day.lower().startswith("a") and hours == 12:
            hours = 0
        elif time_of_day.lower().startswith("p") and hours != 12 :
            hours += 12
        decimal_hours = int(hours) + int(mins) / 60
        return decimal_hours

if __name__ == "__main__":
    main()
