from ldap3 import Server, Connection, Tls
try:
    from ConfigParser import SafeConfigParser, NoOptionError
except ImportError:
    from configparser import SafeConfigParser, NoOptionError


class Config(object):
    def __init__(self, configfile):
        self._parser = SafeConfigParser()
        self._parser.read(configfile)

        self.tls = self._tls_config()
        self.server = self._server_config()
        self.conn = self._conn_config()

    def _tls_config(self):
        if self._parser.has_section('tls'):
            pass
        else:
            return None

    def _server_config(self):
        if self._parser.has_item('ldap', 'uri'):
            uri = self._parser.get('ldap', 'uri')
        else:
            raise NoOptionError

        if self._parser.has_item('ldap', 'port'):
            port = self._parser.has_item('ldap', 'port')
        else:
            port = None

        return Server(host=uri, port=port, tls=self.tls)
