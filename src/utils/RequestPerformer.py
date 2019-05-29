import requests

class RequestPerformer(object):
    def __init__(self):
        self.requestClient = requests
    
    def get(self, url, params):
        response = self.requestClient.get(url, params)
        if response.ok:
            return response.json()
        raise Exception("Request to " + url + " failed")
