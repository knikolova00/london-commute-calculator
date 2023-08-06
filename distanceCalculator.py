from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('API_KEY')


def commuteCalculator(origin, destination, api_key):

    # url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}'
    # url = f'https://api.distancematrix.ai/distancematrix?origins={origin}&destinations={destination}&transit_mode=rail&key={api_key}'
    url = f'https://api.distancematrix.ai/maps/api/distancematrix/json?origins={origin}&destinations={destination}&transit_mode=rail&key={api_key}'
    payload = {}
    headers = {}

    # # Data
    # origin = 'Westminster Abbey,London SW1P 3PA,United Kingdom'
    # destination = 'St John\'s Church,London SW6 1PB, United Kingdom'

    response = requests.get(url, headers=headers, data=payload)
    data = response.json()
    print(response.text)
    try:
        return data['rows'][0]['elements'][0]['duration']['text']
    except IndexError:
        print("List index out of range. Check if 'rows' or 'elements' are empty.")
        return None
    except KeyError:
        print("'duration' key not found in the data. Check the API response.")
        return None


def client():
    origin = input('Where are you?(<street,postcode,country>): ')
    destinations = [
        'Baker Street Station,London NW1 5LA,United Kingdom']
    # destination = input('Where do you want to go?: ')
    # get api from .env
    result = commuteCalculator(origin, destinations, api_key)
    print(result)

# Write result to a txt file


def writeToFile(result):
    with open('result.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    client()
