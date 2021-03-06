import json


class ConfigurationManager:
    """
    Class that deals with getting and setting all the configurations
    """
    __instance = None
    __CONFIG_FILE_PATH = 'data/config.json'

    def __init__(self):
        """
        Sets up the config class for use
        """
        self.__load_config_data()

    def __load_config_data(self):
        """
        Loads data from the config file into memory.
        Note: Separate because of sync issues in persis_config and set_config methods
        :return: None
        """
        config_fh = open(ConfigurationManager.__CONFIG_FILE_PATH)
        self.__config_data = json.load(config_fh)

    def get_config(self, config_key):
        """
        Gets a configuration from the Config file which is loaded in memory
        :param config_key: One of ConfigurationKey
        :return: Value of the configuration key
        """
        try:
            return self.__config_data[config_key]
        except KeyError:
            return None

    def set_config(self, config_key, config_value):
        """
        Sets a config value into memory. Will be persisted later.
        :param config_key: Key of the configuration
        :param config_value: Value of the Configuration
        :return: None
        """
        self.__config_data[config_key] = config_value
        # TODO Decide if persistance is done on every set call
        # If we persist on every set call then potential problem is that on every read call we have to sync
        # Otherwise we would be dealing with stale data.
        self.persist_config()

    def persist_config(self):
        """
        Persist the object as a json file
        :return: None
        """
        config_fh = open(ConfigurationManager.__CONFIG_FILE_PATH, 'w')
        json.dump(self.__config_data, config_fh)

    @staticmethod
    def get_instance():
        """
        Singleton access method
        :return: ConfigurationManager
        """
        if ConfigurationManager.__instance is None:
            ConfigurationManager.__instance = ConfigurationManager()
        return ConfigurationManager.__instance
