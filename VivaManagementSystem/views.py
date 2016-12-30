"""
File that is used to process all the view request
"""
from django.http import HttpResponse
from django.template import loader
from .models import Faculty

def guide_allotment(request):
    query_results = Faculty.objects.all()
    template = loader.get_template('newVMS/guide-allot.html')
    context = {'query_results': query_results}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('VivaManagementSystem/page_login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('newVMS/page_index.html')
    context = {
        'username': 'Deltatiger',
        'pagename': 'Viva Management System - Home'
    }
    return HttpResponse(template.render(context, request))