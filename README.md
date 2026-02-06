# gj-image-pdf-converter
A CLI tool built with Python to automatically convert JPG images into PDF files. Features error handling, dynamic filename generation, and input sanitization using the Pillow library.

#  Image to PDF Converter

A simple and efficient Python script to convert images (`.jpg`) into PDF files directly from the terminal.

##  Features

This project was developed to automate file conversion and practice Python logic. Key features include:

* **User Interaction:** Prompts the user for the filename via the CLI.
* **Robust Error Handling:** Uses `try/except` blocks to prevent crashes if the file is not found.
* **Input Sanitization:** Automatically checks and fixes the file extension (adds `.jpg` if missing).
* **Dynamic Output:** Generates the PDF with the same name as the original image (e.g., `vacation.jpg` becomes `vacation.pdf`).
* **Image Processing:** Automatically converts color modes to RGB to ensure PDF compatibility.

##  Technologies

* **Python 3**
* **Pillow (PIL)** - Python Imaging Library.

##  How to Use

1.  Clone this repository.
2.  Install the required dependency:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script:
    ```bash
    python conversor.py
    ```
4.  Type the name of your image (e.g., `my_photo`) and the PDF will be generated in the same folder.

---
Developed by [Gustavo SJ]
