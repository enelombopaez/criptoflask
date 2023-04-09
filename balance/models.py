
from datetime import datetime
import sqlite3
import requests

from secretdata import securedata

apikey = securedata.get('API_KEY')

headers = {
    'X-CoinAPI-Key': apikey
}

api_url = 'https://rest.coinapi.io'
endpoint = '/v1/exchangerate/BTC/USD'

url = api_url + endpoint

headers = {
    'X-CoinAPI-Key' : apikey
}

response = requests.get(url, headers=headers)
status_code = response.status_code

if status_code == 200:
    print("El restultado de la consulta es:")
    print(response.text)
    print(response.headers)

else:
    print("La peticion a la API ha fallado")
    print(f'el codigo de error es {status_code}')
    print(f'Motivo del error {response.reason}')
    print(response.text)
    print(response.headers)
