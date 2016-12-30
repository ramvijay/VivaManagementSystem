from django.http import JsonResponse
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Student, Tutor
from util import SessionHandler


class StudentAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        tutor = Tutor.objects.select_related().filter(faculty=SessionHandler.get_user_id()).first()
        student_list = Student.objects.filter(course_id=tutor.course.course_id).values('roll_no', 'name', 'organization_name', 'domain_key_word', 'phone_number')
        print(student_list.count())
        return JsonResponse({'result': list(student_list)})
