from fpdf import FPDF

name = input("Name: ")
name = name + " took CS50"

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Arial", style='B', size=48)
pdf.cell(0, 60, "CS50 Shirtificate", align='C')


image_width = 180
image_x = (pdf.w - image_width) / 2
image_y = 70

pdf.image(
    "shirtificate.png",
    x=image_x,
    y=image_y,
    w=image_width
)

pdf.set_auto_page_break(False)

pdf.set_text_color(255, 255, 255)
pdf.set_font("Arial", size=22)
pdf.set_xy(image_x, 130)
pdf.cell(image_width, 10, name, align="C")


pdf.output("shirtificate.pdf")