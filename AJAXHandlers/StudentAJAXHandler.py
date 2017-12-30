from django.http import JsonResponse
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Student, Tutor
from util import SessionHandler

class StudentAJAXHandler(IAJAXHandler):
    '''
    AJAX Handler for getting the Student List from the Server
    '''
    def handle_request(self, http_request):
        # Check the details based on the User Session
        course_id = http_request.GET.get("course_id")
        student_list = Student.objects.filter(course_id=course_id).values('roll_no', 'name', 'course_id','organization_name', 'domain_key_word', 'phone_number').order_by('roll_no')
        return JsonResponse({'result': list(student_list)})
