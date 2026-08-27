import validators

def main():
    # print(email_validator(input("What's your email address? ").strip()))
    email = input("What's your email address? ").strip()
    print(email_validator(email))

def email_validator(email):
    if validators.email(email):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
