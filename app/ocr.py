from paddleocr import PaddleOCR
import fitz  # PyMuPDF

# Initialize OCR engine
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = []
    for page in doc:
        pix = page.get_pixmap()
        image = pix.tobytes("png")
        result = ocr.ocr(image, cls=True)  # <-- corrected this line
        lines = [line[1][0] for line in result[0]]
        all_text.extend(lines)
    return all_text