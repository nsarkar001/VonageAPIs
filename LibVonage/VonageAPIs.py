import requests
import json
import os
import logging
import inspect

class VonageAPIs:
    def __init__(self):
        '''
        Logging is initialized
        '''
        #CReate JWT token and set to some object variable
        self.logs = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.abspath(os.path.join(self.logs, "..", "LogVonage"))

    def getRequests(self, url, payload):
        '''
        This method is used to pass url and payload to the get request.
        It also contains the token for authorization which is obtaned using jwt token method
        :param url:
        :param payload:
        :return:
        '''
        vlog = inspect.stack()
        log_cls = vlog[1][0].f_locals["self"].__class__.__name__
        log_cls = log_cls + ".log"
        log_file = os.path.join(self.log_dir, log_cls)
        print("VonageAPI:{0}".format(log_file))
        #logging.basicConfig(filename=log_file)
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDE2MjAwMDgsImV4cCI6MTY0NDIxMjAwOCwianRpIjoidXEwcHpKak9UM0VCIiwiYXBwbGljYXRpb25faWQiOiJmZjI4NGE2Yi03OTQyLTQwNDQtOWQzNi1kNzc4ZjBjMDBmOTEifQ.EVP8bcx1876eCgwWAUzj_eAteji4gezfqOhawnhR9sKiWJqmcjwY9lmcxoMTvWLa04wDr0vrYkWTzUxCxC6T1YYExlVjzUHrgT5rtQIJX2QVJz0kPnRYMiStDFHHRo502_Eq2NUysJiTViAoOKvrlfwnD2O4MLOxZxPEDK-Ddofvi7JNkclFEvDIQUm8nWKfXUfQnLFpcSAJ5658tEQu1N-VfPNy3fPLSpLe93VwD7Mdhh1TevOm5XoU0AiU1zdNg4I-KeHnZFHk_TRFvFLh59JRrsOhtZm08_jcV7qkNonI3ghU4f75fSNK1cYUIBSOm16OwXhLItOtB3idzpCqXg'
        }
        try:
                response = requests.request("GET", url, headers=headers, data=payload)
                print(response.text)
                return response.status_code, response.json()
        except:
                logging.error("Exception: Failed to get conversation list")

    def postRequests(self, url, payload):
        '''
        This method is used to post requests to conversation api.
        :param url:
        :param payload:
        :return:
        '''
        vlog = inspect.stack()
        log_cls = vlog[1][0].f_locals["self"].__class__.__name__
        log_cls = log_cls + ".log"
        log_file = os.path.join(self.log_dir, log_cls)
        print("VonageAPI:{0}".format(log_file))
        # logging.basicConfig(filename=log_file)
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDE2MjAwMDgsImV4cCI6MTY0NDIxMjAwOCwianRpIjoidXEwcHpKak9UM0VCIiwiYXBwbGljYXRpb25faWQiOiJmZjI4NGE2Yi03OTQyLTQwNDQtOWQzNi1kNzc4ZjBjMDBmOTEifQ.EVP8bcx1876eCgwWAUzj_eAteji4gezfqOhawnhR9sKiWJqmcjwY9lmcxoMTvWLa04wDr0vrYkWTzUxCxC6T1YYExlVjzUHrgT5rtQIJX2QVJz0kPnRYMiStDFHHRo502_Eq2NUysJiTViAoOKvrlfwnD2O4MLOxZxPEDK-Ddofvi7JNkclFEvDIQUm8nWKfXUfQnLFpcSAJ5658tEQu1N-VfPNy3fPLSpLe93VwD7Mdhh1TevOm5XoU0AiU1zdNg4I-KeHnZFHk_TRFvFLh59JRrsOhtZm08_jcV7qkNonI3ghU4f75fSNK1cYUIBSOm16OwXhLItOtB3idzpCqXg',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            #print(response.text)
            return response.status_code, response.json()
        except(msg):
            logging.error("Exception: Failed to create conversation"+ msg)

    def putRequests(self, url, payload):
        '''
        This mehod is used to put requests for updating conversation api
        :param url:
        :param payload:
        :return:
        '''
        vlog = inspect.stack()
        log_cls = vlog[1][0].f_locals["self"].__class__.__name__
        log_cls = log_cls + ".log"
        log_file = os.path.join(self.log_dir, log_cls)
        print("VonageAPI:{0}".format(log_file))
        # logging.basicConfig(filename=log_file)
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDE2MjAwMDgsImV4cCI6MTY0NDIxMjAwOCwianRpIjoidXEwcHpKak9UM0VCIiwiYXBwbGljYXRpb25faWQiOiJmZjI4NGE2Yi03OTQyLTQwNDQtOWQzNi1kNzc4ZjBjMDBmOTEifQ.EVP8bcx1876eCgwWAUzj_eAteji4gezfqOhawnhR9sKiWJqmcjwY9lmcxoMTvWLa04wDr0vrYkWTzUxCxC6T1YYExlVjzUHrgT5rtQIJX2QVJz0kPnRYMiStDFHHRo502_Eq2NUysJiTViAoOKvrlfwnD2O4MLOxZxPEDK-Ddofvi7JNkclFEvDIQUm8nWKfXUfQnLFpcSAJ5658tEQu1N-VfPNy3fPLSpLe93VwD7Mdhh1TevOm5XoU0AiU1zdNg4I-KeHnZFHk_TRFvFLh59JRrsOhtZm08_jcV7qkNonI3ghU4f75fSNK1cYUIBSOm16OwXhLItOtB3idzpCqXg',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("PUT", url, headers=headers, data=payload)
            #print(response.text)
            return response.status_code, response.json()
        except(msg):
            logging.error("Exception: Failed to update conversation"+ msg)

