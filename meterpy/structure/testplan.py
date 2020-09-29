from typing import Union
from meterpy.basics.elements import TestElement
from meterpy.basics.props import SimpleProp, ElementProp
from meterpy.structure.uservariables import UserVariables
import xml.dom.minidom as xml
import os.path


class TestPlan(TestElement):
    def __init__(self,
                 test_name,
                 user_variables: UserVariables,
                 test_class = "TestPlan",
                 gui_class = "TestPlanGui",
                 type = "TestPlan",
                 enabled= True,
                 comments = "",
                 functional_mode = False,
                 teardown_on_shutdown = True,
                 serialize_threadgroups = False,
                 user_define_classpath = ""):
        self.test_class = test_class
        self.gui_class = gui_class
        self.test_name = test_name
        self.enabled = enabled
        self.type = type
        self.prop_list = []
        self.element_list = []

        self.add_prop(user_variables)

        self.add_prop(SimpleProp(f"{self.type}.comments","string",comments))
        self.add_prop(SimpleProp(f"{self.type}.fucntional_mode","bool",functional_mode))
        self.add_prop(SimpleProp(f"{self.type}.tearDown_on_shutdown","bool",teardown_on_shutdown))
        self.add_prop(SimpleProp(f"{self.type}.serialize_threadgroups","bool",serialize_threadgroups))
        self.add_prop(SimpleProp(f"{self.type}.user_define_classpath","string",user_define_classpath))

    def to_xml(self):
        return xml.parseString(str(self)).toprettyxml()

    def to_file(self):
        if os.path.exists(f'{self.test_name}.jmx'):
            os.remove(f'{self.test_name}.jmx')

        jmeter_file = open(f'{self.test_name}.jmx',"w")
        jmeter_file.write(self.to_xml())
        jmeter_file.close()
