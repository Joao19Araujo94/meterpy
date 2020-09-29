from meterpy.basics.props import ElementProp, CollectionProp, SimpleElementProp, SimpleProp

class UserVariables(ElementProp):
    def __init__(self,
                 element_name,
                 variables: dict,
                 element_type = "Arguments",
                 gui_class = "ArgumentsPanel",
                 test_class = "Arguments",
                 test_name = "User Defined Variables",
                 enabled = True):
        self.element_name = element_name + ".user_defined_variables"
        self.element_type = element_type
        self.gui_class = gui_class
        self.test_class = test_class
        self.test_name = test_name
        self.enabled = enabled
        self.prop_list = []

        collection_prop = CollectionProp("Arguments.arguments")

        for key, value in variables.items():
            simple_element_prop = SimpleElementProp(key,"Argument")
            simple_element_prop.add_prop(SimpleProp("Argument.name","string",key))
            simple_element_prop.add_prop(SimpleProp("Argument.value","string",value))
            simple_element_prop.add_prop(SimpleProp("Argument.metadata","string","="))
            collection_prop.add_prop(simple_element_prop)

        self.add_prop(collection_prop)