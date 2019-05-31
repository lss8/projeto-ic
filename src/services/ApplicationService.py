import os
from src.services import ContextAnalysisApiService, WeatherApiService

class ApplicationService(object):
    MINIMUM_INPUT_CONFIDENCE = os.environ["MINIMUM_INPUT_CONFIDENCE"]

    def __init__(self):
        self.context_analysis_api_service = ContextAnalysisApiService()
        self.weather_api_service = WeatherApiService()

    def handle_user_input(self, input, city):
        input_analysis = self.context_analysis_api_service.get_phrase_analysis

        if (input_analysis["confidence"] < MINIMUM_INPUT_CONFIDENCE):
            raise Exception("Input could not produce a valid result")

        if (input_analysis["label"] == "rain"):
            return self.weather_api_service.is_raining_on_city_tomorrow(city)
        elif (input_analysis["label"] == "snow"):
            return self.weather_api_service.is_snowing_on_city_tomorrow(city)
        elif (input_analysis["label"] == "sunny"):
            return self.weather_api_service.is_sunny_on_city_tomorrow(city)
        else:
            return self.weather_api_service.get_city_tomorrow_weather_forecast(city)
