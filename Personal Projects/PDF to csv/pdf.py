# Import the required Module
import tabula

# Read a PDF File
df = tabula.read_pdf("HHOct23.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("HHOct23.pdf", "HHOct23.csv", output_format="csv", pages='all')
print(df)