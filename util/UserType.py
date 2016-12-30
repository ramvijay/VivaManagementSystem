"""
Types of the users in the system.
"""
from enum import Enum


class UserTypes(Enum):
    """
    Various types of the users throughout the system
    """
    SuperAdmin = 1,
    VivaCoordinator = 2,
    Tutor = 3,
    HOD = 4,
    CourseCoord = 5

"""
The type of the tutor will be stored separately in another field.
The second type field will have the course for which the user is pointing to.
"""