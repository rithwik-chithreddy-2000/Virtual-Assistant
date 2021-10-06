import config
import geocoder
import requests
import re
import random
import json


with open(config.JSON_PATH + 'pairs.json', 'r') as file:
    pairs = json.load(file)


def weather(command):
    ''' 
    Gets the temperature of any city or the current city
    :param command: command received by the user
    :returns the temperature of the city in the form of a string
    '''
    city = geocoder.ip('me').city
    city_name = city if command.split(' in ')[-1]==command \
                     else command.split(' in ')[-1]
    
    complete_url = config.WEATHER_API_URL + 'appid=' + \
                   config.WEATHER_API_KEY + '&q=' + city_name
    response = requests.get(complete_url)
    x = response.json()
    
    if x['cod'] != '404':
        y = x['main']
        current_temperature = y['temp'] - 273
        return ' '.join(('Temperature in', city_name.title(),
                        'is', str(round(current_temperature, 2)),
                        'degree Celsius'))
    else:
        return 'City Not Found. Can you repeat it again?'


# Currently not working, so commented
# def jokes():
#     ''' 
#     Tells a random joke
#     :returns the random joke said to the user
#     '''
#     data = requests.get(config.JOKE_URL)
#     a = json.loads(data.text)
#     alexa_say('I have a ' + a['type'] + ' joke')
#     alexa_say(a['setup'])
#     alexa_say(a['punchline'])


def check(command):
    '''
    Checks if the given command exists in pairs
    :param command: command received by the user
    :returns True or False
    '''
    for pattern in pairs:
        if re.search(pattern, command):
            return True
    return False


def reply(command):
    '''
    Gives appropriate response according to the command
    :param command: command received by the user
    :returns string that is said to the user
    '''
    for pattern, response in pairs.items():
        if re.search(pattern, command):
            return random.choice(response)