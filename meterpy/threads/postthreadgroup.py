from meterpy.threads.threadgroup import ThreadGroup

class PostThreadGroup(ThreadGroup):
    def __init__(self,
                 test_name= "tearDown Thread Group",
                 comments= "",
                 enabled= True,
                 loops= 1,
                 continue_forever= False):
        self.test_class = "PostThreadGroup"
        self.gui_class = "PostThreadGroupGui"
        self.test_name = test_name
        self.comments = comments
        self.enabled = enabled
        self.prop_list = []