"""
Method for handling the AJAX Login requests
"""
from django.http import JsonResponse
from django.core.exceptions import MultipleObjectsReturned
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import GuideStudentMap, VMS_Session

class GuideAllotmentStatusAJAXHandler(IAJAXHandler):
    '''
    Invoked from the index page.
    Returns the dict of the various Locations and count of people in those locations
    '''
    def handle_request(self, http_request):
        # Select the current session. is_active is true
        try:
            active_session = VMS_Session.objects.get(is_current=1)
        except MultipleObjectsReturned:
            # Too many current sessions.
            return JsonResponse({'status' : False, \
                                    'msg' : 'Multiple sessions marked is_current=1.\
                                             Only one active session allowed.'})
        # The current session should not be null either
        if active_session is None:
            return JsonResponse({'status': False, \
                                 'msg': 'No session marked with is_current=1'})
        # Get the details of the courses using active_session
        guide_data = self.get_guide_allot_status(active_session)

        return JsonResponse({'status': True, 'data': guide_data})

    def get_guide_allot_status(self, active_session):
        '''
        Method to get the Count of alloted students for each Faculty.
        '''
        student_mappings = GuideStudentMap.objects.filter(session=active_session)
        guide_count_mapping = dict()
        for mapping in student_mappings:
            guide_full_name = mapping.guide.name + '##' + mapping.guide.short_name
            if guide_full_name in guide_count_mapping:
                guide_count_mapping[guide_full_name] += 1
            else:
                guide_count_mapping[guide_full_name] = 1
        return guide_count_mapping
        