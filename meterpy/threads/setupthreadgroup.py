from meterpy.threads.threadgroup import ThreadGroup

class SetupThreadGroup(ThreadGroup):
    def __init__(self,
                 test_name= "setUp Thread Group",
                 comments= "",
                 enabled= True,
                 loops= 1,
                 continue_forever= False):
        self.test_class = "SetupThreadGroup"
        self.gui_class = "SetupThreadGroupGui"
        self.test_name = test_name
        self.comments = comments
        self.enabled = enabled
        self.prop_list = []