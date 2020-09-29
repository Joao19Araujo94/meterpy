from typing import Union
from meterpy.basics.props import SimpleProp, ElementProp, CollectionProp, SimpleElementProp

class Element:
    def __init__(self,
                 type,
                 test_class,
                 gui_class,
                 test_name,
                 enabled= True):
        self.test_class = test_class
        self.gui_class = gui_class
        self.test_name = test_name
        self.enabled = enabled
        self.type = type
        self.prop_list = []
        self.element_list = []

    def add_prop(self,
                 prop: Union[SimpleProp, ElementProp, CollectionProp, SimpleElementProp]):
        if not isinstance(prop, (SimpleProp, ElementProp, CollectionProp, SimpleElementProp)):
            raise TypeError(f"Prop has to be of type SimpleProp, ElementProp. {type(prop)} is not compatible.")
        else:
            self.prop_list.append(prop)

class BaseElement(Element):
    def __init__(self,
                 type,
                 test_class,
                 gui_class,
                 test_name,
                 enabled= True):
        self.test_class = test_class
        self.gui_class = gui_class
        self.test_name = test_name
        self.enabled = enabled
        self.type = type
        self.prop_list = []
        self.element_list = []

    def __str__(self):
        header = f'<?xml version="1.0" encoding="UTF-8"?><jmeterTestPlan version="1.2" properties="5.0" jmeter="5.3"><hashTree>'
        header = header + f'<{self.test_class} guiclass="{self.gui_class}" testclass="{self.test_class}" testname="{self.test_name}" enabled="{self.enabled}">'
        content = ''
        for prop in self.prop_list:
            content = content + str(prop)
        content = content + f'</{self.test_class}><hashTree>'
        for element in self.element_list:
            content = content + str(element)
        content = content + f'</hashTree>'
        footer = f'</hashTree></jmeterTestPlan>'
        return header + content + footer

    def add_element(self,
                    element: Element):
        if not isinstance(element, (Element)):
            raise TypeError(f"Element has to be of type Element. {type(element)} is not compatible.")
        else:
            self.element_list.append(element)

class TestElement(Element):
    def __init__(self,
                 type,
                 test_class,
                 gui_class,
                 test_name,
                 enabled= True):
        self.test_class = test_class
        self.gui_class = gui_class
        self.test_name = test_name
        self.enabled = enabled
        self.type = type
        self.prop_list = []
        self.element_list = []

    def __str__(self):
        header = f'<{self.test_class} guiclass="{self.gui_class}" testclass="{self.test_class}" testname="{self.test_name}" enabled="{self.enabled}">'
        content = ''
        for prop in self.prop_list:
            content = content + str(prop)
        content = content + f'</{self.test_class}><hashTree>'
        for element in self.element_list:
            content = content + str(element)
        footer = f'</hashTree>'
        return header + content + footer

    def add_element(self,
                    element: Element):
        if not isinstance(element, (Element)):
            raise TypeError(f"Element has to be of type Element. {type(element)} is not compatible.")
        else:
            self.element_list.append(element)