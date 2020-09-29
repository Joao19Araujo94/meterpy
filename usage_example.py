from meterpy.structure.testplan import TestPlan
from meterpy.threads.basicthreadgroup import BasicThreadGroup
from meterpy.structure.uservariables import UserVariables
from meterpy.structure.authorization import Authorization
from meterpy.structure.header import Header
from meterpy.samplers.http import HttpSampler, HttpAuthManager, HttpHeaderManager

# Create a set of User Variables which are required to run the TestPlan (Can be empty)
# uv = UserVariables()
uv = UserVariables({"Server_Host":"127.0.0.1","Foo":"Bar"})

# Create a Test Plan with a given name, and user variables
tp = TestPlan("WorkLoad",uv)

# Create a new ThreadGroup with some settings and add to the test plan
tg = BasicThreadGroup(test_name="querySalesEntity",number_of_threads=15,ramp_up_time=0)

# Create HTTP Authorization
# auths = [Authorization("https://postman-echo.com/basic-auth","postman","password","","")]
# auths_manager = HttpAuthManager(auths)

# GET using no parameters with authorization
# http_request = HttpSampler("Postman","postman-echo.com","","https","/basic-auth","GET")
# http_request.add_element(auths_manager)

# Create HTTP Header
# headers = [Header("Content-Type","application/json"), Header("Accept","*/*"), Header("Connection","keep-alive"), Header("Example","Test")]
# headers_manager = HttpHeaderManager(headers)

# GET using no parameters with authorization
# http_request = HttpSampler("Postman","postman-echo.com","","https","/headers","GET")
# http_request.add_element(headers_manager)

# GET using Query String Parameters
# http_request = HttpSampler("Postman","www.postman-echo.com","","https","/get","GET",arguments={"foo1":"bar1","foo2":"bar2"})

# POST using Query String Parameters
# http_request = HttpSampler("Postman","www.postman-echo.com","","https","/post","POST",arguments={"hand":"wave"})

# POST using Payload
# payload = "{hand:wave}"
# http_request = HttpSampler("Postman","www.postman-echo.com","","https","/post","POST",payload=payload)

# tg.add_element(http_request)
# tp.add_element(tg)

# Convert the Test Plan to XML and write a JMX file
# tp.to_file()

# Open JMeter and execute warmup
# tp.execute()