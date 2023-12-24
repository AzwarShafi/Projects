import requests
API_KEY = 'f275fea3c6a5a44d7d8d23ae41f66134'
BASE_URL = 'http://api.coinlayer.com/live'

CURRENCY = input('Enter to track price of Cryptourrencies: ')
request_url = f'http://api.coinlayer.com/live?access_key={API_KEY}&symbols={CURRENCY}'
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    brief = data['rates']
    print(brief)
else:
    print('An Error Occured') 
