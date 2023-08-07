from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('BING_API_KEY')
tfl_primary_key = os.getenv('TFL_PRIM_KEY')
tfl_secondary_key = os.getenv('TFL_SEC_KEY')


def getLatLng(address, api_key):
    endpoint = 'https://dev.virtualearth.net/REST/v1/Locations'
    params = {
        'query': address,
        'key': api_key
    }
    response = requests.get(endpoint, params=params)
    data = response.json()

    if data['statusCode'] == 200 and data['resourceSets'] and data['resourceSets'][0]['resources']:
        coordinates = data['resourceSets'][0]['resources'][0]['point']['coordinates']
        return tuple(coordinates)
    else:
        print('Error: No results found')
        return None


def commuteCalculator(origin, destination, api_key):

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
    result = getLatLng(origin, api_key)
    print(result)
    # result = commuteCalculator(origin, destinations, api_key)
    # print(result)

# Write result to a txt file


def writeToFile(result):
    with open('result.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    client()
