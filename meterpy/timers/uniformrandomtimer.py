from meterpy.timers.timer import Timer
from meterpy.basics.props import SimpleProp

class UniformRandomTimer(Timer):
    def __init__(self,
                 delay,
                 range,
                 enabled = True):
        self.type = "UniformRandomTimer"
        self.test_class = "UniformRandomTimer"
        self.gui_class = "UniformRandomTimerGui"
        self.test_name = "Uniform Random Timer"
        self.enabled = enabled
        self.delay = delay
        self.range = range
        self.prop_list = []

        # Add input parameters to the prop list
        self.add_prop(SimpleProp("ConstantTimer.delay","string",self.delay))
        self.add_prop(SimpleProp("RandomTimer.range","string",self.range))