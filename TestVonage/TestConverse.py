import ast
import json

from LibVonage.VonageAPIs import VonageAPIs
import requests
import logging
import os
import json

class TestConverse:
    def __init__(self):
        '''
        Logging is initialized
        '''
        self.logs = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.abspath(os.path.join(self.logs, "..", "LogVonage"))
        log_file = os.path.join(self.log_dir, "TestConverse.log")
        logging.basicConfig(filename=log_file,filemode='w',level=logging.INFO)


    def testConverse(self, name, display_name):
        '''
        This test method will verify whether a conversation is created successfully
        :param name:
        :param display_name:
        :return:
        '''
        vapis = VonageAPIs()
        payload_str = ('{"name":"' + str(name) + '", "display_name":"' + str(display_name) + '"}')

        #Removing // from the payoad string
        result = ast.literal_eval(payload_str)
        print(result)
        #payload = json.dumps('{"name":' + str(name) + ', "display_name":' + str(display_name)+'}')
        #payload_str = ('{"name":"' + str(name) + '", "display_name":"' + str(display_name)+'"}')
        #print("payload str----", payload_str)

        payload = json.dumps(result)
        #print(payload)
        responseVAPIs, data = vapis.postRequests("https://api.nexmo.com/v0.1/conversations", payload)
        print((responseVAPIs))
        print((data))
        if responseVAPIs == 200 and data['id'] != 0:
            print("pass")
            logging.info("TEST CASE: CREATE CONVERSATION: PASS: Conversation created successfully {0}".format(data['id']))
        else:
            logging.error("TEST CASE: CREATE CONVERSATION: FAIL: Conversation creation failed {0}".format(data['description']))
