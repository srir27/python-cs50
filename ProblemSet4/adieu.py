import inflect

p = inflect.engine()

names = []
while True:
    try:
        usr_input = input("Name: ")
        names.append(usr_input)
        continue

    except (KeyboardInterrupt, EOFError):
        print()
        break

result = p.join(names)
print(f"Adieu, adieu, to {result}")