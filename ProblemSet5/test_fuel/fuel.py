def main():
    while True:
        user_input = input("Fraction: ")
        try:
            z = convert(user_input)
            print(gauge(z))
            break
        except (ZeroDivisionError, ValueError):
            continue

def convert(fraction):
    if "/" in fraction:
        fraction = fraction.split("/")
    else:
        raise ValueError
    if len(fraction) != 2:
        raise ValueError
    x = int(fraction[0])
    y = int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError
    percentage = round(x / y * 100)
    return percentage

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()