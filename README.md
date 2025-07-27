```markdown
# 🧾 Store Receipt Printing App

A lightweight, offline-capable desktop web application built with **Flask** that lets you collect customer purchase data, generate clean PDF receipts using **ReportLab**, and send them to a **thermal printer or any default system printer**.

## 📌 Overview

This project is ideal for small businesses, mini stores, or individual entrepreneurs who want a **simple, fast, and local receipt generation system**. The app collects transaction data from a web form and outputs a printable PDF receipt.

---

## 🚀 Features

- 🔧 Built with **Python Flask**
- 📄 Generates receipts as **PDF files** using `reportlab`
- 🖨️ Supports direct **printing from browser or system command**
    - **Linux:** `lp` command
    - **Windows:** Launches `SumatraPDF` to print silently
- 💡 Lightweight and **works offline**
- 📱 Mobile-responsive interface
- 📂 Saves PDF receipts locally
- ⚡ Fast and easy to use — no external database required

---

## 🛠️ Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Backend    | Python 3, Flask     |
| PDF Engine | ReportLab           |
| Frontend   | HTML, CSS           |
| Printing   | lp (Linux), SumatraPDF (Windows) |

---

## 📷 Screenshots

> ![View](/static/media/Screenshot%20from%202025-07-27%2020-01-05.png)

---

## 🧾 Sample Use Case

1. Enter customer's **name**, **items bought**, **price**, and **payment method**.
2. Click **"Save & Print"**.
3. The system:
    - Generates a PDF receipt.
    - Prints it automatically based on the operating system.

---

## 📂 Project Structure

```

receipt\_app/
│
├── static/                   # Static files (images, CSS, etc.)
│   └── styles.css
│
├── templates/                # HTML templates
│   └── index.html
│
├── receipts/                 # Auto-created folder to store PDFs
│
├── app.py                    # Flask app
├── requirements.txt          # Python dependencies
├── start\_windows.bat         # Windows batch script for SumatraPDF print
├── README.md                 # You're reading it

````

---

## 🖥️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/receipt-printing-app.git
cd receipt-printing-app
````

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Running the App

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🖨️ Printing Configuration

### 🐧 Linux (CUPS-based Printers)

Ensure your printer is set as default and CUPS is installed.

Flask will call:

```bash
lp receipts/receipt_filename.pdf
```

### 🪟 Windows (Using SumatraPDF)

* Download portable [SumatraPDF](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html)
* Place `SumatraPDF.exe` in the project root or update the path in `app.py`
* The app uses:

```cmd
SumatraPDF.exe -print-to-default -silent receipts\receipt.pdf
```

> You can also run `start_windows.bat` for quick testing.

---

## 🧪 Example PDF Output

The generated PDF includes:

* Store name and header
* Date and time
* Customer name, item list, price, payment method
* Footer message (e.g., Thank you)

---

## 🖼️ Styling

The `static/styles.css` file contains basic styles. You can enhance the dropdown, buttons, or layout using custom CSS or frameworks like Bootstrap.

---

## 🌐 Deployment

### Render or Replit

You can deploy this to [Render](https://render.com) or [Replit](https://replit.com), but **PDF printing will only work on systems with printer access**. For web deployment, disable automatic printing or provide download button only.

---

## ✅ Requirements

* Python 3.7+
* Flask
* ReportLab
* `lp` (for Linux) or `SumatraPDF.exe` (for Windows)

---

## 📄 requirements.txt

```txt
Flask
reportlab
```

---

## ❓ FAQ

### Does it work offline?

✅ Yes, once installed, no internet is needed.

### Can I use it on Windows?

✅ Yes. Just make sure you have SumatraPDF.exe available.

### Can I modify the receipt layout?

🛠️ Yes. Modify the `reportlab` drawing section in `app.py`.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! You can:

* Add inventory tracking
* Export reports
* Enhance the UI

---

## 📜 License

MIT License. Free to use, modify, and distribute.

---

## 👨‍💻 Author

**Busari Abdulhakeem Tunde (Alphakeem Adroit)**
📧 \[alphakeem12@gmail.com]
🔗 \[https://www.https://www.linkedin.com/in/akeem-tunde-busari/]
🌍 \[https://www.github.com/Aalphakeem-Adroit/]

---

> 💬 *"Designed for simplicity. Built for small businesses."*
