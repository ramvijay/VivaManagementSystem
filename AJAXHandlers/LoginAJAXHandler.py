"""
Method for handling the AJAX Login requests
"""
import json
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from VivaManagementSystem.models import User
from util.SessionHandler import SessionHandler


class LoginAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        """
        Gets the username and password from the Request and then validates them from the DB
        :param http_request:
        :return: JSON response with the valid flag
        """

        userid = http_request.POST['userid']
        password = http_request.POST['password']
        # TODO have to check for already logged in status
        if SessionHandler.is_user_logged_in():
            return "User already logged in."
        result = dict()
        result['status'] = 'fail'
        try:
            user_obj = User.objects.get(user_id=userid, user_pass=password)
            result['status'] = 'success'
            result['role'] = user_obj.user_role
            SessionHandler.login_user(user_obj)
        except User.DoesNotExist:
            # Invalid user. Return error message
            result['msg'] = 'Invalid credentials.'
        # JSON Encode the results and send it back
        return json.dumps(result)
