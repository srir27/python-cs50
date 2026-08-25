def main():
    userinput = input("Enter you text with emoticons: ")
    userinput = convert(userinput)
    print(userinput)

def convert(userinput):
    userinput = userinput.replace(":)", "🙂")
    userinput = userinput.replace(":(", "🙁")
    return userinput

main()