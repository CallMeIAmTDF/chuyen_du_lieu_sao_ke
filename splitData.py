import math
from PyPDF2 import PdfWriter, PdfReader
inputpdf = PdfReader(open("data.pdf", "rb"))
numOfPages = len(inputpdf.pages)

numOfFiles = math.ceil(numOfPages / 400)
for i in range(1, numOfFiles + 1):
    output = PdfWriter()
    for j in range((i - 1)*400, i*400):
        print(f"load trang thu {j}")
        output.add_page(inputpdf.pages[j])
        with open("./pdfs/data%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)