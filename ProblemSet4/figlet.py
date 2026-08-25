import pyfiglet
import sys

font = None

if len(sys.argv) == 1:
    pass

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")

    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

usr_input = input("Input: ")

try:
    if font:
        print(pyfiglet.figlet_format(usr_input, font=font))
    else:
        print(pyfiglet.figlet_format(usr_input))
        
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")


