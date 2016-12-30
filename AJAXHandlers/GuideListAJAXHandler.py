from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Faculty
from django.http import JsonResponse
from django.core import serializers

class GuideListAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        guide_list = list(Faculty.objects.filter(is_guide=1))
        flag = 1
        if guide_list == []:
            flag = 0
            guide_list = list(Faculty.objects.all())
        return JsonResponse({'result': serializers.serialize('python', guide_list), 'flag': flag})
