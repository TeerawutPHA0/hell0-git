import os
import base64
import json

# Function to convert PDF to Base64
def pdf_to_base64(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()
        base64_data = base64.b64encode(pdf_bytes)
        return base64_data.decode('utf-8')

# Function to convert PDFs in a folder to JSON
def convert_pdfs_in_folder_to_json(folder_path):
    pdf_json = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            base64_data = pdf_to_base64(file_path)
            pdf_json.append({
                "Base64": base64_data,
                "Name": filename
            })
    return pdf_json

# Prompt user to input the folder path containing PDF files
folder_path = input("ป้อนเส้นทางของโฟลเดอร์ที่มีไฟล์ PDF: ")

# Convert PDF files in the folder to JSON
pdf_json = convert_pdfs_in_folder_to_json(folder_path)

# Convert JSON object to string
json_string = json.dumps(pdf_json, indent=4)

# Write JSON data to a text file
with open('pdf_jsonFFF2.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(json_string)

print("การแปลงไฟล์ PDF ในโฟลเดอร์เป็น Base64 เสร็จสิ้น และข้อมูลถูกเขียนลงในไฟล์ pdf_jsonFFF.txt แล้ว")
