from typing import Union

class Prop:
    def __init__(self,
                 element_name,
                 element_type):
        self.element_name = element_name
        self.element_type = element_type

    def get_name(self):
        return self.element_name

    def get_type(self):
        return self.element_type

class SimpleProp(Prop):
    def __init__(self,
                 element_name,
                 element_type,
                 value):
        self.element_name = element_name
        self.element_type = element_type
        self.value = value

    def __str__(self):
        return f'<{self.element_type}Prop name="{self.element_name}">{self.value}</{self.element_type}Prop>'

    def get_value(self):
        return self.value

class ElementProp(Prop):
    def __init__(self,
                 element_name,
                 element_type,
                 gui_class,
                 test_class,
                 test_name,
                 enabled):
        self.element_name = element_name
        self.element_type = element_type
        self.gui_class = gui_class
        self.test_class = test_class
        self.test_name = test_name
        self.enabled = enabled
        self.prop_list = []

    def __str__(self):
        header = f'<elementProp name="{self.element_name}" elementType="{self.element_type}" guiclass ="{self.gui_class}" testclass="{self.test_class}" testname="{self.test_name}" enabled="{self.enabled}">'
        content = ''
        for prop in self.prop_list:
            content = content + str(prop)
        footer = f'</elementProp>'
        return header + content + footer

    def add_prop(self, new_prop: Union[Prop]):
        if not isinstance(new_prop, (Prop)):
            raise TypeError(f"New prop must be of type: Prop. {type(new_prop)} is not allowed.")
        else:
            self.prop_list.append(new_prop)

class SimpleElementProp(Prop):
    def __init__(self,
                 element_name,
                 element_type):
        self.element_name = element_name
        self.element_type = element_type
        self.prop_list = []

    def __str__(self):
        header = f'<elementProp name="{self.element_name}" elementType="{self.element_type}">'
        content = ''
        for simple_prop in self.prop_list:
            content = content + str(simple_prop)
        footer = f'</elementProp>'
        return header + content + footer

    def add_prop(self,
                    prop: Union[SimpleProp]):
        if not isinstance(prop, (SimpleProp)):
            raise TypeError(f"Prop has to be of type SimpleProp. {type(prop)} is not compatible.")
        else:
            self.prop_list.append(prop)

class CollectionProp(Prop):
    def __init__(self,
                 element_name):
        self.element_name = element_name
        self.prop_list = []

    def __str__(self):
        header = f'<collectionProp name="{self.element_name}">'
        content = ''
        for simple_element_prop in self.prop_list:
            content = content + str(simple_element_prop)
        footer = f'</collectionProp>'
        return header + content + footer

    def add_prop(self,
                 prop: Union[SimpleElementProp]):
        if not isinstance(prop, (SimpleElementProp)):
            raise TypeError(f"Prop has to be of type SimpleElementProp. {type(prop)} is not compatible.")
        else:
            self.prop_list.append(prop)

class DoubleProp(Prop):
    def __init__(self,
                 element_name,
                 value,
                 saved_value):
        self.element_name = element_name
        self.element_type = "double"
        self.value = value
        self.saved_value = saved_value

    def __str__(self):
        return f'<{self.element_type}Prop><name>{self.element_name}</name><value>{self.value}</value><savedValue>{self.saved_value}</savedValue></{self.element_type}Prop>'