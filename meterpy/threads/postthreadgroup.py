from meterpy.basics.elements import Element
from meterpy.basics.props import SimpleProp
from meterpy.threads.maincontroller import MainController
from meterpy.threads.threadgroup import ThreadGroup

class PostThreadGroup(ThreadGroup):
    def __init__(self,
                 test_name= "tearDown Thread Group",
                 enabled= True,
                 on_sample_error = "continue",
                 loops= 1,
                 continue_forever= False,
                 number_of_threads = 1,
                 ramp_up_time = 1,
                 scheduler = False,
                 duration = "",
                 delay = "",
                 same_user_on_next_iter = True):
        self.test_class = "PostThreadGroup"
        self.gui_class = "PostThreadGroupGui"
        self.type = "ThreadGroup"
        self.test_name = test_name
        self.enabled = enabled
        self.on_sample_error = on_sample_error
        self.loops = loops
        self.continue_forever = continue_forever
        self.number_of_threads = number_of_threads
        self.ramp_up_time = ramp_up_time
        self.scheduler = scheduler
        self.duration = duration
        self.delay = delay
        self.same_user_on_next_iter = same_user_on_next_iter
        self.prop_list = []
        self.element_list = []

        # Transform input parameters into Prop objects
        self.add_prop(SimpleProp(f"{self.type}.on_sample_error","string",self.on_sample_error))
        self.add_prop(SimpleProp(f"{self.type}.num_threads","string",self.number_of_threads))
        self.add_prop(SimpleProp(f"{self.type}.ramp_time","string",self.ramp_up_time))
        self.add_prop(SimpleProp(f"{self.type}.scheduler","bool",self.scheduler))
        self.add_prop(SimpleProp(f"{self.type}.duration","string",self.duration))
        self.add_prop(SimpleProp(f"{self.type}.delay","string",self.delay))
        self.add_prop(SimpleProp(f"{self.type}.same_user_on_next_iteration","bool",self.same_user_on_next_iter))

        # Add Loop Controller
        self.add_prop(MainController(self.continue_forever,self.loops))