import configparser
import os

config = configparser.ConfigParser()
#config_path = os.path.join(os.path.abspath(os.curdir), "configurations", "config.ini")
#config_path = os.path.join(os.getcwd(), "configurations", "config.ini")
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configurations", "config.ini")
config.read(config_path)
#config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")
print(config_path)
print("Sections found:", config.sections())
#print(open(config_path).read())


class ReadProperties:

    @staticmethod
    def get_base_url():
        return config.get("commonInfo", "base_url")  # fixed 'abc' -> 'commonInfo'

    @staticmethod
    def get_user_name():
        return config.get("credentials", "email")  # fixed section + key

    @staticmethod
    def get_user_password():
        return config.get("credentials", "password")  # fixed section + key






