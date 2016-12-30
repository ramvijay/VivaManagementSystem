import json

from django.http import JsonResponse

from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Faculty
from django.core import serializers


class FacultyListAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        faculty_list = list(Faculty.objects.all())
        return JsonResponse({'result': serializers.serialize('python', faculty_list)})
