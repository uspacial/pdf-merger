import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"✅ Merged PDF saved as: {output_filename}")

if __name__ == "__main__":
    files = [f for f in os.listdir() if f.endswith('.pdf')]
    print("📄 PDFs found:", files)
    merge_pdfs(files, "merged_output.pdf")
