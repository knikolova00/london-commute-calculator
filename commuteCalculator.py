from dotenv import load_dotenv
import requests
import os

load_dotenv()

# API Keys are kept private in a .env file
api_key = os.getenv('BING_API_KEY')
tfl_primary_key = os.getenv('TFL_PRIM_KEY')
tfl_secondary_key = os.getenv('TFL_SEC_KEY')

destinations = [
    'Baker Street Station,London NW1 5LA,United Kingdom', 'Oxford Street,London W1D 1BS,United Kingdom',
    'Harbour Exchange Square, London E14 9GE, United Kingdom', 'Hommerton Hospital, London E9 6SR, United Kingdom',
    'Goldsmiths University, London, UK']


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


def commuteCalculator(originCoords, destinationCoords, destinationAddress):

    base_url = "https://api.tfl.gov.uk/Journey/JourneyResults/"
    url = f"{base_url}{originCoords[0]},{originCoords[1]}/to/{destinationCoords[0]},{destinationCoords[1]}"

    params = {
        'mode': 'tube,dlr,overground,tram,dlr',
        'app_key': tfl_primary_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'journeys' in data and len(data['journeys']) > 0:
        journey = data['journeys'][0]
        # print(
        #     f"{journey['duration']} minutes to get to {destinationAddress}")
        writeToFile(
            f"{journey['duration']} minutes to get to {destinationAddress}")
    else:
        print('Error: No results found')

    # Test origin
    # origin = 'Westminster Abbey,London SW1P 3PA,United Kingdom'


def client():
    origin = input('Where are you?(<street,postcode,country>): ')
    originCoords = getLatLng(origin, api_key)

    for destination in destinations:
        destinationCoords = getLatLng(destination, api_key)
        commuteCalculator(originCoords, destinationCoords, destination)


# Write result to a txt file

def writeToFile(result):
    with open('result.txt', 'a') as f:
        f.write(result + '\n')


# Run the script
if __name__ == '__main__':
    client()
