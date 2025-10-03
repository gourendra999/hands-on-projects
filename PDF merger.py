from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("How many pdfs you want to merge: "))
for i in range(0,n):
    name_pdf=input(f"Enter name the of PDF #{i+1}: ")
    pdfs.append(name_pdf)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()