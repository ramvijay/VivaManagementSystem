"""
Module that contains common utils for the various models in the sytem
"""
from VivaManagementSystem.models import VMS_Session, Student
from django.core.exceptions import MultipleObjectsReturned

class ModelUtils:
    '''
    Container class for all the Utils
    '''
    @staticmethod
    def get_current_session():
        '''
        Gets the session with the is_current flag set to 1.
        Returns: VMS_Session | None
            VMS_Session object if only 1 row has the is_current flag.
            None otherwise.
        '''
        try:
            current_session = VMS_Session.objects.get(is_current=1)
        except MultipleObjectsReturned:
            print("Multiple records have is_current flag set in VMS_Session table.")
            return None
        return current_session
    
    @staticmethod
    def get_current_session_students():
        '''
        Method that returns all Students studying in the current Session.

        :return: List of Student Records
        '''
        current_session = ModelUtils.get_current_session()
        if current_session is None:
            return []
        return Student.objects.filter(session=current_session)
        pass
