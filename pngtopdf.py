from fpdf import FPDF

png_count = 846
png_width = 754
png_height = 1077
png_directory = directory = "./stutzmanthiele/"

pdf = FPDF(orientation="P", unit="pt", format=(png_width, png_height))
pdf.set_margins(0, 0, 0)

pdf.add_page()

for png in range(png_count):
    pdf.image(png_directory + str(png).zfill(3) + ".png", w=png_width, h=png_height)

pdf.output("./stutzmanthiele.pdf", "F")
