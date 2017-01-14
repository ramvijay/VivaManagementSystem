"""
Method for handling the AJAX Login requests
"""
import json
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import Student

class StudentCompanyGraphAJAXHandler(IAJAXHandler):
    '''
    Invoked from the index page.
    Returns the dict of the various Locations and count of people in those locations
    '''
    def handle_request(self, http_request):
        company_names_dict = dict()
        for student in Student.objects.all():
            if student.organization_name.lower() in company_names_dict:
                company_names_dict[student.organization_name.lower()] += 1
            else:
                company_names_dict[student.organization_name.lower()] = 1
        # Format the list according to Morris Chart format
        return_data = []
        for company in company_names_dict.keys():
            company_entry = dict()
            company_entry['label'] = company.title()
            company_entry['value'] = company_names_dict[company]
            return_data.append(company_entry)
        return json.dumps(return_data)
