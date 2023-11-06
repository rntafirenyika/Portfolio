"""
Prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf.
"""

from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", "B", 50)
pdf.cell(0, 40, "CS50 Shirtificate", 0, 1, "C")
pdf.image("shirtificate.png", x=0, y=60)
pdf.set_font("Times", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 180, f"{name} took CS50", 0, 1, "C")
pdf.output("shirtificate.pdf")
