from meterpy.basics.props import SimpleElementProp

class Authorization(SimpleElementProp):
    def __init__(self,
                 url,
                 username,
                 password,
                 domain,
                 realm):
        self.element_name = ""
        self.element_type = "Authorization"
        self.url = url
        self.username = username
        self.password = password
        self.domain = domain
        self.realm = realm
