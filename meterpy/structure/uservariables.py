from meterpy.basics.props import ElementProp, CollectionProp, SimpleElementProp, SimpleProp

class UserVariables(ElementProp):
    """
    This class represents an implementation of the ElementProp class, in the form of user variables.

    It takes a dictionary which will later be used by JMeter to read the input variables
    that can be used throughout the entire test plan.

    Attributes
    ----------
    element_name : str
        a fixed string with "TestPlan.user_defined_variables" as is required by JMeter for this block
    element_type : str
        a fixed string with "Arguments" as is required by JMeter for this block
    gui_class : str
        a fixed string with "ArgumentsPanel" as is required by JMeter for this block. Allows the
        loading of the correct GUI component
    test_class : str
        a fixed string with "Arguments" as is required by JMeter for this block
    test_name : str
        a fixed string with "User Defined Variables" as is required by JMeter for this block
    enabled : bool
        flag that shows if the element should be enabled or disabled
    prop_list : list
        A list of Prop, or Prop extending objects which contain the translated values from the dictionary

    Methods
    -------
    """

    def __init__(self,
                 variables: dict = {}):
        """
        Creates an User Variables object

        If the variables parameter is not passed, and empty dictionary is assumed

        Parameters
        ----------
        variables : dict
            Python dictionary which contains the user defined variables, in a key-value fashion

        Raises
        ------
        TypeError
            If the Prop objects being added to the prop_list are not of a valid type
        """

        self.element_name = "TestPlan.user_defined_variables"
        self.element_type = "Arguments"
        self.gui_class = "ArgumentsPanel"
        self.test_class = "Arguments"
        self.test_name = "User Defined Variables"
        self.enabled = True
        self.prop_list = []

        # Create a collection prop which will hold all the various user variables
        collection_prop = CollectionProp("Arguments.arguments")

        # For each user defined variable, create a new SimpleElementProp, then create
        # a SimpleProp which will hold the key-value properties
        for key, value in variables.items():
            simple_element_prop = SimpleElementProp(key,"Argument")
            simple_element_prop.add_prop(SimpleProp("Argument.name","string",key))
            simple_element_prop.add_prop(SimpleProp("Argument.value","string",value))
            simple_element_prop.add_prop(SimpleProp("Argument.metadata","string","="))
            # For this set of key, value add the created prop to the CollectionProp
            collection_prop.add_prop(simple_element_prop)

        # Add all the created props into the user variables object list
        self.add_prop(collection_prop)