import json

from AJAXHandlers.IAJAXHandler import IAJAXHandler
from django.http import JsonResponse
from VivaManagementSystem.models import Tutor,VMS_Session,Course,Batch,Faculty,User
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

class TutorSetupConfigAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        data_string = http_request.POST.get("result")
        action = http_request.POST.get("action");

        if(action=="GET"):
            session = VMS_Session.objects.get(is_current=True)
            Batch_Data = list(Batch.objects.select_related('course').filter(session=session))
            Batch_Data.sort(key=lambda x: x.course.course_name, reverse=False)
            return JsonResponse({'result':serializers.serialize('json',Batch_Data)})



        if(action=="SET"):
            jsondata = json.loads(data_string)
            session = VMS_Session.objects.get(is_current=True)
            for data in jsondata:

                course = Course.objects.get(course_name=data["course"])
                try:
                    batch = Batch.objects.get(session=session, course=course)
                    faculty = Faculty.objects.get(employee_id=data["tutor"])
                    tutor = Tutor.objects.get(course=course)
                    user = User.objects.get(user_id=tutor.faculty)
                    user.user_id = faculty
                    user.save()
                    tutor.faculty = faculty
                    tutor.save()
                    batch.strength = data["no_of_students"]
                    batch.email_id = data["mail"]
                    batch.tutor = tutor.faculty
                    batch.save()
                except ObjectDoesNotExist:
                    faculty = Faculty.objects.get(employee_id=data["tutor"])
                    tutor = Tutor(session=session,faculty=faculty,course=course)
                    tutor.save()
                    batch = Batch(course=course,tutor=tutor.faculty,strength=data["no_of_students"],email_id=data["mail"])
                    batch.save()
                    user = User(user_pass=course.short_name+"_tutor",user_role="tutor",user=faculty)
                    user.save()
            return JsonResponse({'result': 'success'})
        return JsonResponse({'result':  'invalid request'})