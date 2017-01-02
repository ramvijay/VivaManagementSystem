from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Faculty, Batch
from django.http import JsonResponse
from django.core import serializers


class UpdateGuidesAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        data = http_request.POST.getlist("input[]")
        Faculty.objects.update(is_guide=0)
        for id in data:
            guide = Faculty.objects.get(employee_id=id)
            guide.is_guide = 1
            guide.save()
        guide_list = list(Faculty.objects.filter(is_guide=1))
        students_count = sum((x.strength for x in Batch.objects.all()))
        recommended_count = students_count / len(guide_list)
        return JsonResponse({'result': serializers.serialize('python', guide_list), 'rc': int(recommended_count)})