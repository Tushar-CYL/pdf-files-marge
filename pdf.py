from pypdf import PdfMerger

pdfs = ['a.pdf', 'b.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("done.pdf")
merger.close()