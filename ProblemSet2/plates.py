def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum():
        if s[0:2].isalpha():
            # print(s)
            if 2 <= len(s) <= 6:
                position = first_num(s)
                if position is None:
                    return True
                else:
                    if s[position] != "0":
                        if s[position:].isdigit():
                            return True
    else:
        return False

def first_num(n):
    first_num = None
    for key, value in enumerate(n):
        if value.isdigit():
            first_num = key
            break
    return first_num

main()