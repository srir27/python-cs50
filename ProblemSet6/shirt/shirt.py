import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_ext = os.path.splitext(sys.argv[1])
output_ext = os.path.splitext(sys.argv[2])
extensions = (".jpg", ".jpeg", ".png")

if not input_ext[1] in extensions or not output_ext[1] in extensions:
    sys.exit("Invalid input")

if input_ext[1] != output_ext[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    ip_image = Image.open(sys.argv[1])

    fitted = ImageOps.fit(ip_image, shirt.size)
    fitted.paste(shirt, shirt)

    fitted.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")