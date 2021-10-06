import languageprocessing as nlp
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from pytz import timezone


def time(command):
    '''
    Tells the time at the current location or any location
    :param command: command received by the user
    :returns the time of any location
    '''
    command = command.replace('time', '').strip()
    place = nlp.remove_stopwords(command);
    if place == '':
        time = datetime.now().strftime('%I:%M %p')
        return 'The current time is ' + time
    else:
        try:
            time = time_place(place).strftime('%I:%M %p')
        except:
            return 'Couldn\'t understand the place'
        else:
            return 'The time in ' + place.title() + ' is ' + time


def time_place(loc):
    '''
    Gets the datetime object of the location given
    :param loc: name of the location
    :returns datetime object of the timezone
    '''
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(loc)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    tz = timezone(result)
    return datetime.now(tz)


def date():
    '''
    Tells today's date and day of the week
    :returns today's day and date
    '''
    today = datetime.today().strftime("%A %d %B, %Y")
    return today