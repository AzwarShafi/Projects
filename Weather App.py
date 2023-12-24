import requests
API_KEY = 'd4d5ee90722c8cdf03afb919985f5cf7'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

CITY = input('enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={CITY}'
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp'] - 274.15
    print(f'Temperature: {round(temp)}°C')
    weather = data['weather'][0]['main']
    print(f'Mostly {weather}')
    humidity = data['main']['humidity']
    print(f'humidity: {humidity}%')
else:
    print('An Error Occured')

