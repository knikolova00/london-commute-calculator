# Commute Calculator Console Application
## Description

This is a simple console app that returns commute time between two locations in London. It uses the Bing Maps API to obtain coordinates for the origin location and the TFL API to obtain the commute time between the two locations. The result is written to a text file.

I made this while flat hunting in London to help me quickly obtain commute times between locations of the flats that I was interested in and locations that I will need to commute to.

## How to use
1. Clone the repository
2. Open the solution in Visual Studio Code (or any other IDE)
3. Install the requests library with pip ```pip install requests```.
4. Obtain a Bing Maps API key from [here](https://www.bingmapsportal.com/). 
5. Obtain a TFL API key from [here](https://api-portal.tfl.gov.uk/).
6. Create a file called ```.env``` in the root directory of the project and add the API keys to it in the following format(make sure to include this to a ```.gitignore``` file):
```BING_API_KEY = '<your bing api key>'```
```TFL_API_KEY = '<your tfl api key>'```
7. Run the program with ```python commuteCalculator.py```