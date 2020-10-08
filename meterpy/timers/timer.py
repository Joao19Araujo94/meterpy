from meterpy.basics.elements import TestElement

class Timer(TestElement):
    def __init__(self,
                 type,
                 test_class,
                 gui_class,
                 test_name,
                 enabled= True):
        self.type = type
        self.test_class = test_class
        self.gui_class = gui_class
        self.test_name = test_name
        self.enabled = enabled
        self.prop_list = []