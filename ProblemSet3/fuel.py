while True:
    user_input = input("Enter: ")
    user_input = user_input.split("/")
    try:
        x = int(user_input[0])
        y = int(user_input[1])
        if x > y:
            continue
        if x < 0:
            continue
        percentage = round(x / y * 100)
        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(f"{percentage}%")
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
