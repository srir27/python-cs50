user_input = input("Expression: ")
parts = user_input.split(" ")
x, y, z = parts
if len(parts) == 3:
    if x.isdigit() and y in ["+", "-", "*", "/"] and z.isdigit():
        x = int(x)
        z = int(z)
        if y == "+":
            print (float(x + z))
            print(result)
        elif y == "-":
            print(float( x - z))
        elif y == "*":
            print(float( x * z))
        elif y == "/":
            print(float( x / z))
        else:
            print("Enter a right operator")
else:
    print("Incorrect expression")
