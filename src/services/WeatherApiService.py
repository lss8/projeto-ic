import os
import datetime
from src.utils import RequestPerformer

class WeatherApiService(object):
    API_BASE_URL = os.environ["OPEN_WEATHER_MAP_API_FORECAST_URL"]
    API_KEY = os.environ["OPEN_WEATHER_MAP_API_KEY"]

    def __init__(self):
        self.request_client = RequestPerformer()

    def get_city_tomorrow_weather_forecast(self, city):
        self.city = city

    def is_raining_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Rain")

    def is_snowing_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Snow")

    def is_sunny_on_city_tomorrow(self, city):
        self.is_weather_phenomenon_happening_in_city_tomorrow(city, "Clear")

    def is_weather_phenomenon_happening_in_city_tomorrow(self, city, phenomenon):
        tomorrow_forecast = self.get_tomorrow_weather_forecast(city)

        for sub_weather_forecast in tomorrow_forecast:
            for prevision in sub_weather_forecast["weather"]:
                if (prevision.main == phenomenon):
                    return True
        return False

    def get_tomorrow_weather_forecast(self, city):
        tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)

        response = self.request_client.get(API_BASE_URL, { "q": city, "appid": API_KEY }),
        week_forecast = response["list"]
        tomorrow_forecast = list()

        for forecast in week_forecast:
            forecast_date = datetime.datetime.fromtimestamp(forecast.dt)
            if(forecast_date.day == tomorrow_date.day):
                tomorrow_forecast.append(forecast)
