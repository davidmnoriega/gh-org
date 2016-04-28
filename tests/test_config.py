import unittest
from StringIO import StringIO
from ldap3 import Server, Connection, Tls
from gh_org.config import Config
# Inspired from Python's own unit tests for ConfigParser
# See https://hg.python.org/cpython-fullhistory/file/tip/Lib/test/test_cfgparser.py


class ConfigParserTest(unittest.TestCase):
    def fromstring(self, string):
        sio = StringIO(string)
        cf = Config(sio)
        return cf

    def test_config(self):
        config_string = (
            "[ldap]\n"
            "uri = ldap://ipa.demo1.freeipa.org\n"
            "binddn = cn=admin,dc=demo1,dc=freeipa,dc=org\n"
            "bindpw = Secret123\n"
            "basedn = dc=demo1,dc=freeipa,dc=org\n"
            )
        config = self.fromstring(config_string)
        self.assertIsInstance(config.server, Server)
        self.assertIsInstance(config.conn, Connection)
        self.assertIsInstance(config.tls, Tls)

    def test_config_read_file(self):
        config = Config('./tests/test_config.ini')
        self.assertIsInstance(config, Config)

if __name__ == '__main__':
    unittest.main()
