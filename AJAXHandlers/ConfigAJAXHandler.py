import json
from AJAXHandlers.IAJAXHandler import IAJAXHandler
from util.configuration.ConfigurationManager import ConfigurationManager


class ConfigAJAXHandler(IAJAXHandler):
    def handle_request(self, http_request):
        """
        Gets the configuration
        :param http_request:
        :return: String Returns the Config value
        """
        config_obj = ConfigurationManager.get_instance()
        config_key = http_request.POST['config_key']
        ret = dict()
        ret['result'] = config_obj.get_config(config_key)
        return json.dumps(ret)