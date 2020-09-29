from meterpy.threads.threadgroup import ThreadGroup

class BasicThreadGroup(ThreadGroup):
    def __init__(self,
                 test_name= "Thread Group",
                 comments= "",
                 enabled= True,
                 loops= 1,
                 continue_forever= False):
        self.test_class = "ThreadGroup"
        self.gui_class = "ThreadGroupGui"
        self.test_name = test_name
        self.comments = comments
        self.enabled = enabled
        self.prop_list = []