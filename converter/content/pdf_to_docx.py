import io
import PyPDF2
import docx

def pdf_to_docx(pdf_file):
    # Create a PyPDF2 reader object from the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Create a new DOCX document
    doc = docx.Document()
    
    # Iterate through each page in the PDF file
    for page_num in range(pdf_reader.numPages):
        # Extract the text from the page
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        
        # Add the text to the DOCX document
        doc.add_paragraph(text)
    
    # Save the DOCX document to a BytesIO buffer
    output = io.BytesIO()
    doc.save(output)
    
    # Reset the buffer to the beginning to allow reading from it
    output.seek(0)
    
    # Return the BytesIO buffer containing the DOCX file
    return output
