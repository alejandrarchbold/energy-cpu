from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Create a PDF file
pdf_file = canvas.Canvas("report.pdf", pagesize=letter)

# Create a plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Plot Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")

# Save plot to PDF
with PdfPages("report.pdf") as pdf:
    pdf.savefig()

# Add text to PDF file
pdf_file.drawString(72, 720, "Report Title")
pdf_file.drawString(72, 700, "Report Subtitle")
pdf_file.showPage()
pdf_file.save()

