def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s.isalnum():
        return False
    if not 2 <= len(s) <= 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    position = first_num(s)
    if position is None:
        return True
    else:
        if s[position] != "0":
            if s[position:].isdigit():
                return True
            else:
                return False
        else:
            return False


def first_num(n):
    first_num = None
    for key, value in enumerate(n):
        if value.isdigit():
            first_num = key
            break
    return first_num

if __name__ == "__main__":
    main()