import requests

class RequestPerformer(object):
    def __init__(self):
        self.request_client = requests

    def get(self, url, params):
        response = self.request_client.get(url, params)
        if response.ok:
            return response.json()
        raise Exception("Request to " + url + " failed")
