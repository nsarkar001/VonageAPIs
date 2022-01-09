import ast
from LibVonage.VonageAPIs import VonageAPIs
import requests
import logging
import os
import json

class TestUpdate:
    def __init__(self):
        '''
        Initializing logging
        '''
        self.logs = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.abspath(os.path.join(self.logs, "..", "LogVonage"))
        log_file = os.path.join(self.log_dir, "TestUpdate.log")
        logging.basicConfig(filename=log_file,filemode='w',level=logging.INFO)


    def testUpdate(self, update_name, conv_id, update_display_name):
        '''
        This test method is to verify whether an existing conversation is be updated successfully based on conversation id
        :param update_name:
        :param conv_id:
        :param update_display_name:
        :return:
        '''
        vapis = VonageAPIs()
        payload_str = ('{"name":"' + str(update_name) + '", "display_name":"' + str(update_display_name) + '"}')
        result = ast.literal_eval(payload_str) #remove // from payload string
        print(result)
        #payload = json.dumps('{"name":' + str(name) + ', "display_name":' + str(display_name)+'}')
        #payload_str = ('{"name":"' + str(name) + '", "display_name":"' + str(display_name)+'"}')
        #print("payload str----", payload_str)

        payload = json.dumps(result)
        #print(payload)

        #Create url with conversation id
        url = "https://api.nexmo.com/v0.1/conversations/{}".format(conv_id)
        responseVAPIs, data = vapis.putRequests(url, payload)
        print((responseVAPIs))
        print((data))

        if responseVAPIs == 200:
            #testList_names(update_name)
            logging.info("TEST CASE: UPDATE CONVERSATION: PASS: Conversation ID {0} updated successfully".format(conv_id))
        else:
            logging.error("TEST CASE: CREATE CONVERSATION: FAIL: Conversation update failed {0}".format(data['description']))
