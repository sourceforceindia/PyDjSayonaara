from django.shortcuts import render, HttpResponse
from django.template import loader
import pprint
import os
# Create your views here
def home(request):
    template = loader.get_template('about.html')
    # Pass argument to template
    context = {
        'remote_addr': request.META['REMOTE_ADDR']
    }
    # template.render()
    # Render template with context
    pprint.pprint(dict(os.environ), width = 1)
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')
