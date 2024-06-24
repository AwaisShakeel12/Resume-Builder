from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ResumeForm
from .models import Resume
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings


def aspremium(request):
    return render(request, 'base/blue.html')
def blackedition(request):
    return render(request, 'base/blackedition.html')


def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            return redirect('generate_pdf', pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, 'base/index.html', {'form': form})

def generate_pdf(request, pk):
    # Getting the resume object
    resume = get_object_or_404(Resume, pk=pk)

    # Getting the HTML template and rendering it with the resume data
    template_name = f'base/{resume.template_choice}.html'
    template = get_template(template_name)
    html = template.render({'resume': resume}, request=request)

    # Making the HTTP response to PDF type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{resume.pk}.pdf"'

    # Converting the HTTP response to a byte stream to convert to PDF
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources.
    """
    # Handle MEDIA files
    if settings.MEDIA_URL and uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    # Handle STATIC files
    elif settings.STATIC_URL and uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        return uri

    # Check if the file exists
    if not os.path.isfile(path):
        raise Exception('File not found: %s' % path)

    return path

