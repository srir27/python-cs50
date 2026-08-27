import re

def main():
    print(count(input("Text: ").strip()))


def count(s):
    pattern = r"\bum\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    #print(matches)
    return len(matches)

if __name__ == "__main__":
    main()
