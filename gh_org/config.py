from ssl import CERT_NONE, CERT_REQUIRED
from ldap3 import Server, Connection, Tls
try:
    from ConfigParser import SafeConfigParser, NoOptionError
except ImportError:
    from configparser import SafeConfigParser, NoOptionError


class Config(object):
    def __init__(self, configfile):
        self._parser = SafeConfigParser()
        if isinstance(configfile, basestring):
            self._parser.read(configfile)
        else:
            self._parser.readfp(configfile)

        if self._parser.has_option('ldap', 'use_tls'):
            self.use_tls = self._parser.getboolean('ldap', 'use_tls')
        else:
            self.use_tls = False

        self.tls = self._tls_config()
        self.server = self._server_config()
        self.conn = self._conn_config()

    def _tls_config(self):
        if self._parser.has_section('tls'):
            try:
                if self._parser.getboolean('tls', 'validate'):
                    validate = CERT_REQUIRED
                else:
                    validate = CERT_NONE
            except NoOptionError:
                validate = CERT_REQUIRED

            try:
                ca_file = self._parser.get('tls', 'ca_file')
            except NoOptionError:
                ca_file = None

            return Tls(validate=validate, ca_certs_file=ca_file)
        else:
            return Tls(validate=CERT_REQUIRED)

    def _server_config(self):
        if self._parser.has_option('ldap', 'uri'):
            uri = self._parser.get('ldap', 'uri')
        else:
            raise NoOptionError

        if self._parser.has_option('ldap', 'port'):
            port = self._parser.has_option('ldap', 'port')
        else:
            port = None

        return Server(host=uri, port=port, tls=self.tls)

    def _conn_config(self):
        try:
            username = self._parser.get('ldap', 'binddn')
            password = self._parser.get('ldap', 'bindpw')
            return Connection(self.server, username, password)
        except NoOptionError:
            raise NoOptionError('Something wrong with your config file')
