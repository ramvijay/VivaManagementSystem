"""
Interface used for all AJAX Calls
"""

from abc import ABCMeta, abstractmethod


class IAJAXHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle_request(self, http_request):
        pass
