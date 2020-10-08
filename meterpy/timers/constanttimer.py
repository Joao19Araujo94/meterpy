from meterpy.timers.timer import Timer
from meterpy.basics.props import SimpleProp

class ConstantTimer(Timer):
    def __init__(self,
                 delay,
                 enabled = True):
        self.type = "ConstantTimer"
        self.test_class = "ConstantTimer"
        self.gui_class = "ConstantTimerGui"
        self.test_name = "Constant Timer"
        self.enabled = enabled
        self.delay = delay
        self.prop_list = []

        # Add inputs parameters to prop list
        self.add_prop(SimpleProp(f'{self.type}.delay',"string",self.delay))