from meterpy.basics.elements import TestElement

class ThreadGroup(TestElement):
    def __init__(self,
                 test_name= "Thread Group",
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
        self.test_class = "ThreadGroup"
        self.gui_class = "ThreadGroupGui"
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