input_string = input("Input: ")
output = ""
vowels = set("aeiouAEIOU")
for i in input_string:
    if i not in vowels:
        output += i
print(output)