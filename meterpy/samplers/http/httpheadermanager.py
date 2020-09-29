from meterpy.basics.elements import TestElement
from meterpy.structure.header import Header
from meterpy.basics.props import SimpleProp, ElementProp, CollectionProp, SimpleElementProp

class HttpHeaderManager(TestElement):
    def __init__(self,
                 header_list: [],
                 enabled= True):
        self.test_class = "HeaderManager"
        self.gui_class = "HeaderPanel"
        self.test_name = "HTTP Header Manager"
        self.enabled = enabled
        self.type = "HeaderManager"
        self.header_list = header_list
        self.prop_list = []
        self.element_list = []

        # Add parameters to prop list
        collection_prop = CollectionProp("HeaderManager.headers")

        for header in self.header_list:
            if not isinstance(header,Header):
                raise TypeError(f'Type {type(header)} is not allowed. Please make sure the authorization list contains only Authorization types.')
            else:
                simple_element_prop = SimpleElementProp(header.element_name, header.element_type)
                simple_element_prop.add_prop(SimpleProp("Header.name","string",header.name))
                simple_element_prop.add_prop(SimpleProp("Header.value","string",header.value))
                collection_prop.add_prop(simple_element_prop)

        # Add collection prop to the element
        self.add_prop(collection_prop)