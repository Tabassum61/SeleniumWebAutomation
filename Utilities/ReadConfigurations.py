from configparser import ConfigParser

def read_configurations(category,key):
    config = ConfigParser()
    config.read("/Users/tabassum.ferdous/PycharmProjects/seleniumproject/Configurations/config_ini")
    return config.get(category,key)
