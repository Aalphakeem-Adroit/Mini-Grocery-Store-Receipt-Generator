from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os
from reportlab.pdfgen import canvas
import tempfile
import subprocess

app = Flask(__name__)
CSV_FILE = 'store_records.csv'

# Ensure CSV exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["DateTime", "Customer Name", "Items", "Price", "Payment Mode", "Phone", "Remarks"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    items = request.form['items']
    price = request.form['price']
    payment = request.form['payment']
    phone = request.form['phone']
    remarks = request.form['remarks']
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = [now, name, items, price, payment, phone, remarks]

    # Save to CSV
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(transaction)

    # Save as PDF
    save_as_pdf(transaction)

    # Print Receipt
    print_receipt(transaction)

    return redirect('/')

def save_as_pdf(transaction):
    headers = ["DateTime", "Customer Name", "Items", "Price", "Payment Mode", "Phone", "Remarks"]
    os.makedirs("receipts", exist_ok=True)
    receipt_num = len(open(CSV_FILE).readlines())
    path = f"receipts/receipt_{receipt_num}.pdf"
    c = canvas.Canvas(path)
    c.setFont("Helvetica", 12)
    y = 800
    for h, t in zip(headers, transaction):
        c.drawString(50, y, f"{h}: {t}")
        y -= 20
    c.save()

def print_receipt(transaction):
    lines = [
        "=== STORE RECEIPT ===",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "-"*32
    ]
    headers = ["Time", "Name", "Items", "Price", "Pay", "Phone", "Note"]
    for h, v in zip(headers, transaction):
        lines.append(f"{h}: {v}")
    lines.append("-"*32)
    lines.append("Thanks for shopping!")
    lines.append("\n\n\n")
    receipt_text = "\n".join(lines)

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp:
        temp.write(receipt_text)
        temp_path = temp.name
    subprocess.run(["lp", temp_path])

if __name__ == '__main__':
    app.run(debug=True)


# ===================

# from flask import Flask, render_template, request, send_file
# from reportlab.pdfgen import canvas
# import os
# import platform
# import subprocess

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     data = {
#         'name': request.form.get('name', ''),
#         'items': request.form.get('items', ''),
#         'price': request.form.get('price', ''),
#         'payment': request.form.get('payment', ''),
#         'phone': request.form.get('phone', ''),
#         'remarks': request.form.get('remarks', ''),
#     }

#     # Create PDF
#     pdf_file = "receipt.pdf"
#     c = canvas.Canvas(pdf_file)
#     c.drawString(100, 800, f"Name: {data['name']}")
#     c.drawString(100, 780, f"Items: {data['items']}")
#     c.drawString(100, 760, f"Price: ₦{data['price']}")
#     c.drawString(100, 740, f"Payment: {data['payment']}")
#     c.drawString(100, 720, f"Phone: {data['phone']}")
#     c.drawString(100, 700, f"Remarks: {data['remarks']}")
#     c.showPage()
#     c.save()

#     # OS Detection
#     os_type = platform.system()
#     if os_type == "Linux":
#         subprocess.run(["lp", pdf_file])
#     elif os_type == "Windows":
#         sumatra_path = r"C:\Program Files\SumatraPDF\SumatraPDF.exe"
#         if os.path.exists(sumatra_path):
#             subprocess.run([sumatra_path, "-print-to-default", pdf_file])
#         else:
#             return "SumatraPDF not found on Windows"
#     else:
#         return "Unsupported OS"

#     return send_file(pdf_file, as_attachment=False)

# if __name__ == '__main__':
#     app.run(debug=True)
