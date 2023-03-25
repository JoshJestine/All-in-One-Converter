import os
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def home(request):
    return render(request, 'content/home.html')

def convert_pdf_to_docx(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        if pdf_file.name.endswith('.pdf'):
            # Create a unique name for the uploaded file to avoid overwriting
            new_filename = str(uuid.uuid4()) + '.pdf'
            temp_path = os.path.join(settings.MEDIA_ROOT, new_filename)
            with open(temp_path, 'wb+') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)
            # Convert the PDF file to DOCX using subprocess and the pdf2docx library
            output_path = os.path.join(settings.MEDIA_ROOT, str(uuid.uuid4()) + '.docx')
            subprocess.run(['pdf2docx', temp_path, output_path])
            # Return the converted DOCX file to the user for download
            with open(output_path, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type='content/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = f'attachment; filename="{pdf_file.name[:-4]}.docx"'
            os.remove(temp_path)  # Remove the temporary PDF file
            os.remove(output_path)  # Remove the converted DOCX file
            return response
    return render(request, 'pdf_to_docx.html')
