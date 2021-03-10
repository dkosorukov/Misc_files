import time
import argparse
from weatherService import WeatherService

def within_time(item, start, end):
    return item['dt'] > start and item['dt'] < end

def makeUmbrellaDecision(city, state, country) -> bool:
    current_time = time.time()
    end_time = current_time + 12*60*60
    wx = WeatherService.getForecast(city, state, country)
    # pick records in the set time interval
    wx = [x for x in wx if within_time(x, current_time, end_time)]
    rain_probability = [x['rain']['3h'] for x in wx if 'rain' in x]
    if len(rain_probability) > 0 and max(rain_probability) > 0.1:
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decide if we need an umbrella.')
    parser.add_argument('--city', type=str, default='san francisco',
                        help='city to check')
    parser.add_argument('--state', type=str, default='ca',
                        help='state to check')                    
    parser.add_argument('--country', type=str, default='us',
                        help='country to check')
    args = parser.parse_args()

    city=args.city
    state=args.state
    country=args.country

    if(makeUmbrellaDecision(city, state, country)):
        print(f'You need an umbrella today in {city}, {state}, {country}')
    else:
        print(f'You do NOT need an umbrella today in {city}, {state}, {country}')