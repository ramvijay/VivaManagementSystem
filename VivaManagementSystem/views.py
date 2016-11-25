"""
File that is used to process all the view request
"""
from django.http import HttpResponse
from django.template import loader
from . import settings


def login(request):
    template = loader.get_template('VivaManagementSystem/page_login.html')
    context = {}
    return HttpResponse(template.render(context, request))
