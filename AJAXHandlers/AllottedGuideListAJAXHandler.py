import json
from django.http import JsonResponse
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Faculty, GuideStudentMap
from util import SessionHandler


class AllottedGuideListAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        user_role = SessionHandler.get_user_role()
        if user_role == "admin":
            return JsonResponse({'map_data': 'no data'})



        guides = Faculty.objects.select_related().filter(is_guide=True)
        map = None
        map_dict = dict()
        for iter_guide in guides:
            mapped_data = GuideStudentMap.objects.select_related('guide').filter(session__session_id=1, guide=iter_guide)
            mapped_students = []
            class student_detail(object):
                student = None
                tutor = None
                course = None

                @staticmethod
                def serialize(obj):
                    return {
                        "student": obj.student,
                        "tutor": obj.tutor,
                      #  "course":obj.course
                    }
            for data in mapped_data:
                student_obj = student_detail()
                student_obj.student = data.student.roll_no
                student_obj.tutor = data.tutor.faculty.employee_id
                student_obj.course = data.tutor.course.course_name
                mapped_students.append(student_obj)
            mapped_students.sort(key=lambda x: x.course, reverse=False)
            map_dict[iter_guide.employee_id] = mapped_students

        return JsonResponse({'map_data': json.dumps(map_dict, default=student_detail.serialize)})
