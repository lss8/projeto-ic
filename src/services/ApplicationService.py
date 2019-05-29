import os
from src.services import ContextAnalysisApiService, WeatherApiService

class ApplicationService(object):
    MINIMUM_INPUT_CONFIDENCE = os.environ["MINIMUM_INPUT_CONFIDENCE"]

    def __init__(self):
        self.contextAnalysisApiService = ContextAnalysisApiService()
        self.weatherApiService = WeatherApiService()

    def handle_user_input(self, input, city):
        inputAnalysis = self.contextAnalysisApiService.get_phrase_analysis

        if (inputAnalysis["confidence"] < MINIMUM_INPUT_CONFIDENCE):
            raise Exception("Input could not produce a result")

        if (inputAnalysis["label"] == "rain"):
            return self.weatherApiService.is_raining_on_city_tomorrow(city)
        elif (inputAnalysis["label"] == "snow"):
            return self.weatherApiService.is_snowing_on_city_tomorrow(city)
        elif (inputAnalysis["label"] == "sunny"):
            return self.weatherApiService.is_sunny_on_city_tomorrow(city)
        else:
            return self.weatherApiService.get_city_tomorrow_weather_forecast(city)
