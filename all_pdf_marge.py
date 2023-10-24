from PyPDF2 import PdfFileMerger
import os


merger = PdfFileMerger()

path_to_files = 'D:\path\PDF-Merger-master\PDF-Merger-master\pdf_files'

for root, dirs, file_names in os.walk(path_to_files):
    for file_name in file_names:
        merger.append(path_to_files + file_name)

merger.write("merged_all_pages.pdf")
merger.close()
