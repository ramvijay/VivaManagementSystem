"""
Factory for creating the AJAX handlers based on the name
"""
from AJAXHandlers.ConfigPageOpenAJAXHandler import ConfigPageOpenAJAXHandler
from AJAXHandlers.GuideListAJAXHandler import GuideListAJAXHandler
from AJAXHandlers.LoginAJAXHandler import LoginAJAXHandler
from AJAXHandlers.CourseModificationAJAXHandler import CourseModificationAJAXHandler
from AJAXHandlers.ConfigAJAXHandler import ConfigAJAXHandler
from AJAXHandlers.SetConfigsAJAXHandler import SetConfigsAJAXHandler
from AJAXHandlers.FacultyListAJAXHandler import FacultyListAJAXHandler
from AJAXHandlers.StudentAJAXHandler import StudentAJAXHandler
from AJAXHandlers.TutorSetupConfigAJAXHandler import TutorSetupConfigAJAXHandler
from AJAXHandlers.UpdateGuidesAJAXHandler import UpdateGuidesAJAXHandler
from AJAXHandlers.AllottedGuideListAJAXHandler import AllottedGuideListAJAXHandler
from AJAXHandlers.UpdateAllottedGuideListAJAXHandler import UpdateAllottedGuideListAJAXHandler
from AJAXHandlers.DeleteAllottedGuideListAJAXHandler import DeleteAllottedGuideListAJAXHandler
from AJAXHandlers.CourseListAJAXHandler import CourseListAJAXHandler
from AJAXHandlers.VMSSessionAJAXHandler import VMSSessionAJAXHandler
from AJAXHandlers.StudentLocationGraphAJAXHandler import StudentLocationGraphAJAXHandler
from AJAXHandlers.StudentCompanyGraphAJAXHandler import StudentCompanyGraphAJAXHandler


class AJAXHandlerFactory:
    @staticmethod
    def create_instance(ajax_call):
        """
        Create the required type of Handler based on the type of the AJAX call.
        :param ajax_call: Name of the AJAX call handler to create
        :return:
        """
        if ajax_call == '':
            return None
        elif ajax_call == 'login':
            return LoginAJAXHandler()
        elif ajax_call == "get_course_list":
            return CourseListAJAXHandler()
        elif ajax_call == 'course_modification':
            return CourseModificationAJAXHandler()
        elif ajax_call == 'get_config':
            return ConfigAJAXHandler()
        elif ajax_call == 'set_configs':
            return SetConfigsAJAXHandler()
        elif ajax_call == 'config_page_open_status':
            return ConfigPageOpenAJAXHandler()
        elif ajax_call == 'get_faculty_list':
            return FacultyListAJAXHandler()
        elif ajax_call == 'get_student_list':
            return StudentAJAXHandler()
        elif ajax_call == 'get_guide_list':
            return GuideListAJAXHandler()
        elif ajax_call == 'update_guides':
            return UpdateGuidesAJAXHandler()
        elif ajax_call == 'get_allotted_guide_list':
            return AllottedGuideListAJAXHandler()
        elif ajax_call == 'update_allotted_guide_list':
            return UpdateAllottedGuideListAJAXHandler()
        elif ajax_call == 'delete_allotted_guide_list':
            return DeleteAllottedGuideListAJAXHandler()
        elif ajax_call == 'vms_session':
            return VMSSessionAJAXHandler()
        elif ajax_call == 'tutor_setup_config':
            return TutorSetupConfigAJAXHandler()
        elif ajax_call == 'student_location_graph':
            return StudentLocationGraphAJAXHandler()
        elif ajax_call == 'student_company_graph':
            return StudentCompanyGraphAJAXHandler()

        return None
