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


def commuteCalculator(originCoords, destinationCoords):

    base_url = "https://api.tfl.gov.uk/Journey/JourneyResults/"
    url = f"{base_url}{originCoords[0]},{originCoords[1]}/to/{destinationCoords[0]},{destinationCoords[1]}"

    params = {
        'mode': 'tube,dlr,overground,tram,dlr',
        'app_key': tfl_primary_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    if 'journeys' in data and len(data['journeys']) > 0:
        journey = data['journeys'][0]
        print(f"Duration: {journey['duration']} minutes")
    else:
        print('Error: No results found')

    # # Data
    # origin = 'Westminster Abbey,London SW1P 3PA,United Kingdom'
    # destination = 'St John\'s Church,London SW6 1PB, United Kingdom'


def client():
    origin = input('Where are you?(<street,postcode,country>): ')
    destinations = [
        'Baker Street Station,London NW1 5LA,United Kingdom']
    # Turnham Green Station,London W4 1LR,United Kingdom
    originCoords = getLatLng(origin, api_key)
    destinationCoords = getLatLng(destinations[0], api_key)
    result = commuteCalculator(originCoords, destinationCoords)
    print(result)

    # result = commuteCalculator(origin, destinations, api_key)
    # print(result)

# Write result to a txt file


def writeToFile(result):
    with open('result.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    client()
