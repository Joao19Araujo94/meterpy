from meterpy.basics.props import SimpleElementProp

class Header(SimpleElementProp):
    def __init__(self,
                 name,
                 value):
        self.element_name = ""
        self.element_type = "Header"
        self.name = name
        self.value = value