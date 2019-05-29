import os
from src.utils import RequestPerformer

class ContextAnalysisApiService(object):
    API_BASE_URL = os.environ["MACHINE_LEARNING_FOR_KIDS_API_CLASSIFY_URL"]

    def __init__(self):
        self.requestClient = RequestPerformer()

    def get_phrase_analysis(self, phrase):
        response = self.requestClient.get(API_BASE_URL, { "data": phrase })
        bestResult = response[0]
        return {
            "label": bestResult["class_name"],
            "confidence": bestResult["confidence"],
        }
