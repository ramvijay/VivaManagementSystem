"""
All submodules required in the index page.
"""

from AJAXHandlers.index_page.TutorDetailsAJAXHandler import TutorDetailsAJAXHandler
from AJAXHandlers.index_page.GuideAllotmentStatusAJAXHandler import GuideAllotmentStatusAJAXHandler
from AJAXHandlers.index_page.StudentCompanyGraphAJAXHandler import StudentCompanyGraphAJAXHandler
from AJAXHandlers.index_page.StudentLocationGraphAJAXHandler import StudentLocationGraphAJAXHandler

__all__ = [
    'TutorDetailsAJAXHandler',
    'GuideAllotmentStatusAJAXHandler',
    'StudentCompanyGraphAJAXHandler',
    'StudentLocationGraphAJAXHandler'
]
