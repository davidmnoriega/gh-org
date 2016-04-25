import unittest
from ldap3 import Server, Connection, Tls
from gh_org.config import Config


class ConfigParserTest(unittest.TestCase):
    def test_config(self):
        config = Config('./tests/test_config.ini')
        self.assertIsInstance(config.server, Server)
        self.assertIsInstance(config.conn, Connection)
        self.assertIsNotInstance(config.tls, Tls)

    def test_config_ssl(self):
        config = Config('./tests/test_config_ssl.ini')
        self.assertIsInstance(config.server, Server)
        self.assertIsInstance(config.conn, Connection)
        self.assertIsInstance(config.tls, Tls)

if __name__ == '__main__':
    unittest.main()
