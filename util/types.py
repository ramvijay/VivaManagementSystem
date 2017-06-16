"""
File that contains all the different Types used in the System
"""
from enum import Enum

# TODO This is not useful at all. Waste of Code.
class UserRoles(Enum):
    """
    Various Roles played by the Faculty in the system
    """
    Admin = 'Administrator'
    VivaCoordinator = 'Viva Coordinator'
    Tutor = 'Tutor'
    Guide = 'Guide'
    Guest = 'Guest' # This is for default users who are not logged in.

    @staticmethod
    def get_type_from_str(str_value):
        '''
        Returns the UserRole based on the string value.
        '''
        for role in UserRoles:
            if role.value == str_value:
                return role
        return UserRoles.Guest
