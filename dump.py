import fitz  # PyMuPDF
import csv

def con(pdf_file, csv_file):
  # Open the PDF file
    doc = fitz.open(pdf_file)

    # Initialize a CSV writer
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Iterate through each page of the PDF
        for page in doc:
            # Extract text from the page
            text = page.get_text()

            # Write the extracted text to the CSV file
            writer.writerow([text.strip()])  # Strip leading/trailing whitespace

    # Close the PDF file
    doc.close()
con('C:\\Users\\AYUSH UMARE\\OneDrive\\Desktop\\sem 2\\DCC4.1.pdf', 'file1.csv')
con('C:\\Users\\AYUSH UMARE\\OneDrive\\Desktop\\sem 2\\DCC4.2.pdf', 'file2.csv')

