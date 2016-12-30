from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Course
from util.configuration.ConfigurationManager import ConfigurationManager
import json


class CourseModificationAJAXHandler(IAJAXHandler):
    """
    Handles everything related to adding and removing for courses.
    """
    def handle_request(self, http_request):
        """
        Does either remove or add operation for the Courses.
        :param http_request: Contains all the HTTP data
        :return: None
        """
        result = dict()
        result['status'] = 'fail'
        action = http_request.POST['action']
        course = http_request.POST['course']
        shortName = http_request.POST['shortName']
        degree = http_request.POST['degree']
        print(action)
        print(course)
        print(shortName)
        if action == 'add':
            newCourse = Course(course_name=course,short_name=shortName,degree_name=degree)
            newCourse.save()
        if action == 'remove':
            print("remove : "+course)
            deleteCourse = Course.objects.filter(course_name=course)
            print(deleteCourse.delete())
        """config_manager = ConfigurationManager.get_instance()
        courses = config_manager.get_config('Courses')
        short_name_mappings = config_manager.get_config('ShortNames')
        if short_name_mappings is None:
            short_name_mappings = dict()
        if action == 'remove':
            if courses is None:
                return json.dumps(result)
            courses.remove(course)
            del short_name_mappings[course]
        else:
            if courses is None:
                courses = []
            courses.append(course)
            short_name_mappings[course] = shortName
        courses = list(sorted(courses))
        config_manager.set_config('Courses', courses)
        config_manager.set_config('ShortNames', short_name_mappings)"""
        result['status'] = 'success'
        return json.dumps(result)

