from barcode import Gs1_128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

data = "SWHPK2406-01234"
data2 = "AASD056-05664"
gs1_data = f"{data}"

def generate_barcode(code, filename):
    barcode = Gs1_128(code, writer=ImageWriter())
    barcode.save(filename)
    return filename + ".png"

def create_pdf_with_barcode(barcode_image, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    img = Image.open(barcode_image)
    img_width, img_height = img.size
    
    c.drawImage(barcode_image, (width - img_width) / 2, (height - img_height) / 2)
    c.showPage()
    c.save()

# ตัวอย่างการใช้งาน
barcode_image = generate_barcode(gs1_data, "barcode") 
create_pdf_with_barcode(barcode_image, "barcode.pdf") 
