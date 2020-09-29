from typing import Union
from meterpy.basics.elements import BaseElement
from meterpy.basics.elements import Element
from meterpy.basics.props import SimpleProp, ElementProp
from meterpy.structure.uservariables import UserVariables
import xml.dom.minidom as xml
import os.path
import subprocess

class TestPlan(BaseElement):
    """
    This class represents an usage for the BaseElement class, in the form of user variables.

    It takes a dictionary which will later be used by JMeter to read the input variables
    that can be used throughout the entire test plan.

    Attributes
    ----------
    gui_class : str
        a fixed string with "TestPlanGui" as is required by JMeter for this block. Allows the
        loading of the correct GUI component
    test_class : str
        a fixed string with "Arguments" as is required by JMeter for this block
    test_name : str
        a fixed string with "User Defined Variables" as is required by JMeter for this block
    type : str
        a fixed string with value
    prop_list : list
        A list of Prop, or Prop extending objects which contain the translated values from the dictionary

    Methods
    -------
    """
    def __init__(self,
                 test_name,
                 user_variables: UserVariables,
                 enabled= True,
                 comments = "",
                 functional_mode = False,
                 teardown_on_shutdown = True,
                 serialize_threadgroups = False,
                 user_define_classpath = ""):
        self.gui_class = "TestPlanGui"
        self.test_class = "TestPlan"
        self.test_name = test_name
        self.enabled = enabled
        self.type = "TestPlan"
        self.prop_list = []
        self.element_list = []

        # Add the user variables to the Prop object list
        self.add_prop(user_variables)

        # Add the program parameters to the Prop object list
        self.add_prop(SimpleProp(f"{self.type}.comments","string",comments))
        self.add_prop(SimpleProp(f"{self.type}.functional_mode","bool",functional_mode))
        self.add_prop(SimpleProp(f"{self.type}.tearDown_on_shutdown","bool",teardown_on_shutdown))
        self.add_prop(SimpleProp(f"{self.type}.serialize_threadgroups","bool",serialize_threadgroups))
        self.add_prop(SimpleProp(f"{self.type}.user_define_classpath","string",user_define_classpath))

    def to_xml(self):
        """
        Converts the Test Plan object to text, recursively
        """

        return xml.parseString(str(self)).toprettyxml()

    def to_file(self):
        """
        Writes the converted XML from Test Plan into a JMX file which can be opened and
        executed in JMeter
        """

        # Check if the file already exists, if it does delete it first
        if os.path.exists(f'{self.test_name}.jmx'):
            os.remove(f'{self.test_name}.jmx')

        # Open, write and close the file. Overwrite if the file exists (Never does)
        jmeter_file = open(f'{self.test_name}.jmx',"w")
        jmeter_file.write(self.to_xml())
        jmeter_file.close()

    def execute(self):
        # Open the JMeter process and execute the file with the test plan given
        p = subprocess.Popen(f'jmeter -n -t {self.test_name}.jmx -l results_{self.test_name}.csv', shell=True, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
