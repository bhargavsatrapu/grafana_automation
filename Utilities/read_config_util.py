import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def get_config_properties(key):
        value = config.get('common info', key)
        return value
