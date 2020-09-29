from meterpy.basics.elements import TestElement
from meterpy.basics.props import SimpleProp, ElementProp, CollectionProp, SimpleElementProp

class HttpSampler(TestElement):
    def __init__(self,
                 test_name,
                 domain,
                 port,
                 protocol,
                 path,
                 method,
                 content_encoding = "",
                 embedded_url_re = "",
                 connect_timeout = "",
                 response_timeout = "",
                 follow_redirects = True,
                 auto_redirects = False,
                 use_keepalive = True,
                 do_multipart_post = False,
                 payload = "",
                 arguments: dict = {},
                 use_equals = True,
                 enabled= True):
        self.test_class = "HTTPSamplerProxy"
        self.gui_class = "HttpTestSampleGui"
        self.type = "HTTPSampler"
        self.test_name = test_name
        self.enabled = enabled
        self.domain = domain
        self.port = port
        self.protocol = protocol
        self.content_encoding = content_encoding
        self.path = path
        self.method = method
        self.follow_redirects = follow_redirects
        self.auto_redirects = auto_redirects
        self.use_keepalive = use_keepalive
        self.do_multipart_post = do_multipart_post
        self.embedded_url_re = embedded_url_re
        self.connect_timeout = connect_timeout
        self.response_timeout = response_timeout
        self.payload = payload
        self.arguments = arguments
        self.use_equals = use_equals
        self.prop_list = []
        self.element_list = []

        # Create ElementProp to hold arguments or payload
        element_prop = ElementProp("HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","User Defined Variables",True)
        collection_prop = CollectionProp("Arguments.arguments")

        # Adjust according to request type
        if self.method.upper() == "POST":
            # Insert POST request arguments
            if not self.payload == "":
                httparguments = SimpleElementProp("","HTTPArgument")
                httparguments.add_prop(SimpleProp("HTTPArgument.always_encode","bool",False))
                httparguments.add_prop(SimpleProp("Argument.value","string",self.payload))
                httparguments.add_prop(SimpleProp("Argument.metadata","string","="))

                # Add to the collection prop to hold all of above
                collection_prop.add_prop(httparguments)
            else:
                # Iterate through the given parameters and fill in the arguments
                for key, value in self.arguments.items():
                    httparguments = SimpleElementProp(key,"HTTPArgument")
                    httparguments.add_prop(SimpleProp("HTTPArgument.always_encode","bool",False))
                    httparguments.add_prop(SimpleProp("Argument.value","string",value))
                    httparguments.add_prop(SimpleProp("Argument.metadata","string","="))
                    httparguments.add_prop(SimpleProp("HTTPArgument.use_equals","bool",True))
                    httparguments.add_prop(SimpleProp("Argument.name","string",key))

                    # Add to the collection prop to hold all of above
                    collection_prop.add_prop(httparguments)

        elif self.method.upper() == "GET":
            # Iterate through the given parameters and fill in the arguments
            for key, value in self.arguments.items():
                httparguments = SimpleElementProp(key,"HTTPArgument")
                httparguments.add_prop(SimpleProp("HTTPArgument.always_encode","bool",False))
                httparguments.add_prop(SimpleProp("Argument.value","string",value))
                httparguments.add_prop(SimpleProp("Argument.metadata","string","="))
                httparguments.add_prop(SimpleProp("HTTPArgument.use_equals","bool",True))
                httparguments.add_prop(SimpleProp("Argument.name","string",key))

                # Add to the collection prop to hold all of above
                collection_prop.add_prop(httparguments)
        else:
            raise NotImplementedError(f'{self.method} is not yet implemented. Please use GET, POST')

        # Add to element prop to be added to the main element
        element_prop.add_prop(collection_prop)

        # Add method specific parameters Prop to sampler
        self.add_prop(element_prop)

        # Transform input parameters into Prop objects and add to prop list
        self.add_prop(SimpleProp(f"{self.type}.domain","string",self.domain))
        self.add_prop(SimpleProp(f"{self.type}.port","string",self.port))
        self.add_prop(SimpleProp(f"{self.type}.protocol","string",self.protocol))
        self.add_prop(SimpleProp(f"{self.type}.contentEncoding","string",self.content_encoding))
        self.add_prop(SimpleProp(f"{self.type}.path","string",self.path))
        self.add_prop(SimpleProp(f"{self.type}.method","string",self.method))
        self.add_prop(SimpleProp(f"{self.type}.follow_redirects","string",self.follow_redirects))
        self.add_prop(SimpleProp(f"{self.type}.auto_redirects","string",self.auto_redirects))
        self.add_prop(SimpleProp(f"{self.type}.use_keepalive","string",self.use_keepalive))
        self.add_prop(SimpleProp(f"{self.type}.DO_MULTIPART_POST","string",self.do_multipart_post))
        self.add_prop(SimpleProp(f"{self.type}.embedded_url_re","string",self.embedded_url_re))
        self.add_prop(SimpleProp(f"{self.type}.connect_timeout","string",self.connect_timeout))
        self.add_prop(SimpleProp(f"{self.type}.response_timeout","string",self.response_timeout))