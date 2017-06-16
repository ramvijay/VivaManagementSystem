"""
Method for handling the AJAX Login requests
"""
import json
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from util.geolocation.geolocation import GeoLocationAPI
from VivaManagementSystem.models import Student

class StudentLocationGraphAJAXHandler(IAJAXHandler):
    '''
    Invoked from the index page.
    Returns the dict of the various Locations and count of people in those locations
    '''
    def handle_request(self, http_request):
        location_dict = dict()
        student_list = []
        for student in Student.objects.all():
            if student.address_city == '':
                try:
                    student.address_city = GeoLocationAPI(student.address_short_url) \
                                                .get_city_from_location()
                except Exception:
                    student.address_city = 'Others'
                student.save()
            if student.address_city in location_dict:
                location_dict[student.address_city] += 1
            else:
                location_dict[student.address_city] = 1
        # Format the list according to Morris Chart format
        return_data = []
        for location in location_dict.keys():
            location_entry = dict()
            location_entry['label'] = location
            location_entry['value'] = location_dict[location]
            return_data.append(location_entry)
        return json.dumps(return_data)
