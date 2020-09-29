class TestPlan:
    def __init__(self, testname= "DefaultTestPlan", comments= "", functionalMode= False, teardown= True, serialize= False):
        self.test_name = testname
        self.comments = comments
        self.functional_mode = functionalMode
        self.teardown_on_shutdown = teardown
        self.serialize_threadgroups = serialize

    def to_xml(self):
        print("xml")