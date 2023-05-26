import csv
from pypdf import PdfReader, PdfWriter

with open('data/meta.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        reader = PdfReader("data/" + row['pdf'])
        writer = PdfWriter()
        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)
        # Add the metadata
        writer.add_metadata({
            "/Author": row['author'],
            "/Title": row['title'],
            "/Subject": row['subject'],
            "/Producer": "The library" 
            }) 
        # Save the new PDF to a file
        with open("data/meta-" + row['pdf'], "wb") as f:
            writer.write(f)
