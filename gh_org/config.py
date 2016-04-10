try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

CONFIG_STRUCT = {'ldap': ['uri', 'binddn', 'bindpw', 'base']}


class Section(object):
    def __init__(self, section, section_dict):
        for item in CONFIG_STRUCT[section]:
            self.__setattr__(item, section_dict[item])


class Config(object):
    def __init__(self, configfile):
        self.__parser = SafeConfigParser()
        self.__parser.read(configfile)

        for section in CONFIG_STRUCT.keys():
            section_dict = dict(self.__parser.items(section))
            self.__setattr__(section, Section(section, section_dict))
