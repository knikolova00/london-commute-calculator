from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('BING_API_KEY')


def commuteCalculator(origin, destination, api_key):

    # url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}'
    # url = f'https://api.distancematrix.ai/distancematrix?origins={origin}&destinations={destination}&transit_mode=rail&key={api_key}'
    url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix'
    querystring = {
        'origins': f'{origin}',
        'destinations': f'{destination}',
        'travelMode': 'transit',
        'timeType': 'arrival',
        'dateTime': 'now',
        'key': f'{api_key}'
    }

    # # Data
    # origin = 'Westminster Abbey,London SW1P 3PA,United Kingdom'
    # destination = 'St John\'s Church,London SW6 1PB, United Kingdom'

    response = requests.get(url, params=querystring)
    data = response.json()
    print(response.text)
    try:
        for row in data['rows']:
            for element in row['elements']:
                duration = element['duration']['text']
                return duration
    except IndexError:
        print("List index out of range. Check if 'rows' or 'elements' are empty.")
        return None
    except KeyError:
        print("'duration' key not found in the data. Check the API response.")
        return None


def client():
    origin = input('Where are you?(<street,postcode,country>): ')
    destinations = [
        'Baker Street Station,London NW1 5LA,United Kingdom;Turnham Green Station,London W4 1LR,United Kingdom']
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
