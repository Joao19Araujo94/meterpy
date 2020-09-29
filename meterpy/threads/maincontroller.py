from meterpy.basics.props import ElementProp, SimpleProp

class MainController(ElementProp):

    def __init__(self,
                 continue_forever,
                 loops):
        self.element_name = f'ThreadGroup.main_controller'
        self.element_type = f'LoopController'
        self.gui_class = f'LoopControlPanel'
        self.test_class = f'LoopController'
        self.test_name = f'LoopController'
        self.enabled = True
        self.continue_forever = continue_forever
        self.loops = loops
        self.prop_list = []

        # Add two SimpleProps to hold the loop configuration
        self.add_prop(SimpleProp(f'LoopController.continue_forever',f'bool',self.continue_forever))
        self.add_prop(SimpleProp(f'LoopController.loops',f'string',self.loops))