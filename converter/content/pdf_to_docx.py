import io
from django.shortcuts import render
from django.http import HttpResponse
import PyPDF2
import docx

def convert_pdf_to_docx(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        # Get the uploaded PDF file from the request
        pdf_file = request.FILES['pdf_file'].read()
        
        # Create a PyPDF2 reader object from the PDF file
        pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(pdf_file))
        
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
        
        # Prepare the response with the DOCX file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="converted.docx"'
        response.write(output.getvalue())
        
        return response
        
    else:
        return render(request, 'converter/pdf_to_docx.html')
