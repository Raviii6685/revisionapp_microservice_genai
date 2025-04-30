import fitz  # PyMuPDF
from PIL import Image
import base64
from io import BytesIO

def convert_pdf_to_base64_images(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=250)
        image = Image.open(BytesIO(pix.tobytes("png")))
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
        images.append(base64_img)
    return images