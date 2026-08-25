def main():
    input_string = input("Input: ")
    print( shorten(input_string))


def shorten(word):
    vowels = set("aeiouAEIOU")
    result = ""
    for i in word:
        if i not in vowels:
            result += i
    return result



if __name__ == "__main__":
    main()