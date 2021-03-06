import requests

class WeatherService:
    appId = ""
    baseUrl = "https://api.openweathermap.org/data/2.5/forecast" #?q={city name},{state code},{country code}&appid={API key}
    @classmethod
    def getForecast(cls, city, state, country):
        response = requests.get(cls.baseUrl, params=[
            ('appid', cls.appId),
            ('q', f'{city}, {state}, {country}')
        ])
        data = response.json()
        return data['list']

if __name__ == "__main__":
    print(WeatherService.getForecast('san francisco', 'ca', 'us'))
    

#
