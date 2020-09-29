from meterpy.basics.elements import TestElement
from meterpy.structure.authorization import Authorization
from meterpy.basics.props import SimpleProp, ElementProp, CollectionProp, SimpleElementProp

class HttpAuthManager(TestElement):
    def __init__(self,
                 authorization_list: [],
                 enabled= True):
        self.test_class = "AuthManager"
        self.gui_class = "AuthPanel"
        self.test_name = "HTTP Authorization Manager"
        self.enabled = enabled
        self.type = "AuthManager"
        self.authorization_list = authorization_list
        self.prop_list = []
        self.element_list = []

        # Add parameters to prop list
        collection_prop = CollectionProp("AuthManager.auth_list")

        for authorization in self.authorization_list:
            if not isinstance(authorization,Authorization):
                raise TypeError(f'Type {type(authorization)} is not allowed. Please make sure the authorization list contains only Authorization types.')
            else:
                simple_element_prop = SimpleElementProp(authorization.element_name, authorization.element_type)
                simple_element_prop.add_prop(SimpleProp("Authorization.url","string",authorization.url))
                simple_element_prop.add_prop(SimpleProp("Authorization.username","string",authorization.username))
                simple_element_prop.add_prop(SimpleProp("Authorization.password","string",authorization.password))
                simple_element_prop.add_prop(SimpleProp("Authorization.domain","string",authorization.domain))
                simple_element_prop.add_prop(SimpleProp("Authorization.realm","string",authorization.realm))

                collection_prop.add_prop(simple_element_prop)

        # Add collection prop to the element
        self.add_prop(collection_prop)