import os
from src.utils import RequestPerformer

class WeatherApiService(object):
    API_BASE_URL = os.environ["OPEN_WEATHER_MAP_API_FORECAST_URL"]
    API_KEY = os.environ["OPEN_WEATHER_MAP_API_KEY"]

    def __init__(self):
        self.requestClient = RequestPerformer()

    def get_city_tomorrow_weather_forecast(self, city):
        self.city = city

    def is_raining_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Rain")

    def is_snowing_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Snow")

    def is_sunny_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Clear")

    def is_weather_phenomenon_happening_in_city_tomorrow(self, city, phenomenon):
        response = self.requestClient.get(API_BASE_URL, { "q": city, "appid": API_KEY })
        tomorrowForecast = response["list"]

        for prevision in tomorrowForecast.weather:
            if (prevision.main == phenomenon):
                return True
        return False


