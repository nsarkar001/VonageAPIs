import json

from LibVonage.VonageAPIs import VonageAPIs
import requests
import logging
import os

class TestList:
    def __init__(self):
        '''
        Initializing logging for test methods
        '''
        self.logs = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.abspath(os.path.join(self.logs, "..", "LogVonage"))
        log_file = os.path.join(self.log_dir, "TestList.log")
        logging.basicConfig(filename=log_file,filemode='w',level=logging.INFO)


    def testList(self, expectedCount):
        '''
        This test method will verify the conversation count for our application

        :param expectedCount:
        :return:
        '''
        vapis = VonageAPIs()
        payload = {}
        responseVAPIs, data = vapis.getRequests("https://api.nexmo.com/v0.1/conversations", payload)
        print(type(responseVAPIs))
        print(type(data))
        #print(data['_embedded'])
        val = dict((data['_embedded']))
        #print(val)
        val1 = val['conversations']
        #print(val1)
        #print(val['conversations'])
        uuid = []
        name = []
        for item in val1:
            print(item)
            for key in item:
                #for i in range(0,len(item)+1):
                    if (key == 'uuid'):
                        uuid.append(item[key])
                    if (key == 'name'):
                        name.append(item[key])

        print("UUID======================",uuid)
        print("Name======================", name)

        actualCount = data['count']
        print(expectedCount)
        print(actualCount)
        if actualCount == expectedCount:
            print("pass")
            logging.info("PASS: Count matched, Expected Count: {0}, Actual Count: {1}".format(expectedCount, actualCount))
        else:
            print("fail")
            logging.error("FAIL: Count not matched, Expected Count: {0}, Actual Count: {1}".format(expectedCount, actualCount))

    def testList_names(self, conv_name):
        '''
        This test method will verify whether the given conversation name exists in the conversation list
        :param conv_name:
        :return:
        '''
        vapis = VonageAPIs()
        payload = {}
        responseVAPIs, data = vapis.getRequests("https://api.nexmo.com/v0.1/conversations", payload)
        print(type(responseVAPIs))
        print(type(data))
        #print(data['_embedded'])
        val = dict((data['_embedded']))
        #print(val)
        val1 = val['conversations']
        #print(val1)
        #print(val['conversations'])
        name = []
        for item in val1:
            print(item)
            for key in item:
                    if (key == 'name'):
                        name.append(item[key])

        print("UUID======================",name)

        if conv_name in name:
            logging.info("TEST CASE: CHECK CONVERSATION NAME: PASS: Name {0} exists in the conversation list".format(conv_name))
        else:
            logging.error("TEST CASE: CHECK CONVERSATION NAME: FAIL: Name {0} does not exists in the conversation list".format(conv_name))

    def testList_ids(self, conv_ids):
        '''
        This test method will verify whether the given id exists in the onversation list
        :param conv_ids:
        :return:
        '''
        vapis = VonageAPIs()
        payload = {}
        responseVAPIs, data = vapis.getRequests("https://api.nexmo.com/v0.1/conversations", payload)
        print(type(responseVAPIs))
        print(type(data))
        #print(data['_embedded'])
        val = dict((data['_embedded']))
        #print(val)
        val1 = val['conversations']
        #print(val1)
        #print(val['conversations'])
        uuid = []
        for item in val1:
            print(item)
            for key in item:
                #for i in range(0,len(item)+1):
                    if (key == 'uuid'):
                        uuid.append(item[key])

        print("UUID======================",uuid)

        if conv_ids in uuid:
            logging.info("TEST CASE: CHECK CONVERSATION ID: PASS: ID {0} exists in the conversation IDs list".format(conv_ids))
        else:
            logging.error("TEST CASE: CHECK CONVERSATION ID: FAIL: ID {0} does not exists in the conversation IDs list".format(conv_ids))