import pytesseract
from pdf2image import convert_from_path
import glob

# test 1 master
# test 2 master
def lambda_handler():
    # PDF file in your local
    pdfs = glob.glob(r"C:/Users/Documents/test.pdf")

    # Tesseract path in your local
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    for pdf_path in pdfs:
        # Poppler path in your local
        pages = convert_from_path(pdf_path, 500, poppler_path = r"C:\Program Files\poppler-0.68.0\bin", )

        for pageNum, imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob, lang='eng')
            print(text)
