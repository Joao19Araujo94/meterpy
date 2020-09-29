from meterpy.structure.testplan import TestPlan
from meterpy.structure.uservariables import UserVariables

uv = UserVariables("TestPlan",{"variavel1":"valor1","variavel2":"valor2"})

tp = TestPlan("WorkLoad",uv)

tp.to_file()
