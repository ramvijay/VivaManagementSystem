import json

from AJAXHandlers.IAJAXHandler import IAJAXHandler
from django.http import JsonResponse
from VivaManagementSystem.models import Tutor,VMS_Session,Course,Batch,Faculty


class TutorSetupConfigAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        data_string = http_request.POST.get("result")
        action = http_request.POST.get("action");

        if(action=="GET"):
            session = VMS_Session.objects.get(is_current=True)


        if(action=="SET"):
            jsondata = json.loads(data_string)
            session = VMS_Session.objects.get(is_current=True)
            for data in jsondata:
                course = Course.objects.get(course_name=data["course"])
                tutor = Tutor(session=session,faculty=Faculty.objects.get(employee_id=data["tutor"]),course=course)
                tutor.save()
                batch = Batch(course=course,year=2016,tutor=tutor.faculty,strength=data["no_of_students"],email_id=data["mail"])
                batch.save()

        return JsonResponse({'result':  'success'})