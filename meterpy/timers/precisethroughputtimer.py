from meterpy.timers.timer import Timer
from meterpy.basics.props import SimpleProp, DoubleProp

class PreciseThroughputTimer(Timer):
    def __init__(self,
                 throughput,
                 throughput_surplus,
                 batch_size = 1,
                 thread_delay = 0,
                 duration = 3600,
                 limit = 10000,
                 random_seed = 0,
                 enabled = True):
        self.type = "PreciseThroughputTimer"
        self.test_class = "PreciseThroughputTimer"
        self.gui_class = "TestBeanGui"
        self.test_name = "Precise Throughput Timer"
        self.enabled = enabled
        self.thread_delay = thread_delay
        self.throughput = throughput
        self.throughtput_surplus = throughput_surplus
        self.batch_size = batch_size
        self.thread_delay = thread_delay
        self.duration = duration
        self.limit = limit
        self.random_seed = random_seed
        self.prop_list = []

        # Add input parameters to the prop list
        self.add_prop(SimpleProp("batchSize","int",self.delay))
        self.add_prop(SimpleProp("batchThreadDelay","int",self.range))
        self.add_prop(SimpleProp("duration","int",self.range))
        self.add_prop(SimpleProp("batchThreadDelay","int",self.range))
        self.add_prop(SimpleProp("batchThreadDelay","int",self.range))
        self.add_prop(SimpleProp("batchThreadDelay","int",self.range))
        self.add_prop(SimpleProp("batchThreadDelay","int",self.range))