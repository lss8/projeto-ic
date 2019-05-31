import os
from src.utils import RequestPerformer

class ContextAnalysisApiService(object):
    API_BASE_URL = os.environ["MACHINE_LEARNING_FOR_KIDS_API_CLASSIFY_URL"]

    def __init__(self):
        self.request_client = RequestPerformer()

    def get_phrase_analysis(self, phrase):
        response = self.request_client.get(API_BASE_URL, { "data": phrase })
        best_result = response[0]
        return {
            "label": best_result["class_name"],
            "confidence": best_result["confidence"],
        }
