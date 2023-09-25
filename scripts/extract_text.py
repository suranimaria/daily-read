import os
import re
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def clear_output_file():
    """Clear the content of the output text file."""
    open("your-path/DailyRead/output/output.txt", "w").close()


def convert_pdf_to_text(pdf_path: str) -> str:
    """
    Convert a PDF file to text.
    
    :param pdf_path: Path to the PDF file.
    :return: Extracted text from the PDF.
    """
    res_manager = PDFResourceManager()
    ret_str = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(res_manager, ret_str, laparams=layout)
    
    with open(pdf_path, 'rb') as file:
        interpreter = PDFPageInterpreter(res_manager, device)
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)

        text = ret_str.getvalue()

    device.close()
    ret_str.close()
    return text.decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract-text.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    clear_output_file()

    # Extract text from the provided PDF
    extracted_text = convert_pdf_to_text(pdf_path)

    # Save the extracted text to the output file
    with open("your-path/DailyRead/output/output.txt", "a", encoding="utf-8") as text_file:
        text_file.write(extracted_text)
