from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('API_KEY')


def commuteCalculator(origin, destination, api_key):
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['rows'][0]['elements'][0]['duration']['text']


def client():
    origin = input('Where are you?: ')
    destination = input('Where do you want to go?: ')
    # get api from .env
    result = commuteCalculator(origin, destination, api_key)
    print(result)
