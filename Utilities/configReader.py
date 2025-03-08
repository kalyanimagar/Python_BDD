from configparser import ConfigParser

def readConfiguration(category,key):
    config=ConfigParser()
    config.read("Configuration/config.ini")
    return config.get(category,key)