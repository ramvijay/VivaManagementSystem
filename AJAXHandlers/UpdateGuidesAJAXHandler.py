from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Faculty, Batch
from django.http import JsonResponse
from django.core import serializers


class UpdateGuidesAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        data = http_request.POST.getlist("input[]")
        print(data)
        Faculty.objects.update(is_guide=0)
        for id in data:
            guide = Faculty.objects.get(employee_id=id)
            guide.is_guide = 1
            guide.save()
        faculty_list = list(Faculty.objects.all())
        guide_count = sum(faculty.is_guide for faculty in faculty_list)
        students_count = sum((x.strength for x in Batch.objects.all()))
        if guide_count == 0:
            guide_count = 1
        recommended_count = students_count / guide_count
        return JsonResponse({'result': serializers.serialize('python', faculty_list), 'rc': int(recommended_count)})