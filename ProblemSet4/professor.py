import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for j in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if ans == x + y:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0 and int(level) <= 3:
            level = int(level)
            return level
        else:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()