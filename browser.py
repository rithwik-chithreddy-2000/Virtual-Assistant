import config
import languageprocessing as nlp
import pywhatkit
import webbrowser
from googlesearch import search


def play_song(command):
    '''
    Plays a song and open it on youtube
    :param command: command received by the user
    :returns string that is said to the user
    '''
    command = command.split('play', 1)[-1].strip()
    platform = None if command.split(' on ')[-1]==command \
                    else command.split(' on ')[-1]
    if platform == 'youtube' or platform == None:
        pywhatkit.playonyt(command)         #Open in youtube
    else:
        #Implement other platforms like spotify if needed
        pass
    return 'Playing ' + command


def searchw(command):
    '''
    Searches a topic and open it in the browser
    :param command: command received by the user
    :returns string that is said to the user
    '''
    command = command.replace('search', '').strip()
    url = config.GGLURL_SEARCH + command.replace(' ','+')
    webbrowser.open(url)
    return 'Opening google search'


def who_is(command):
    '''
    Searches a person and open it on wikipedia
    :param command: command received by the user
    :returns string that is said to the user
    '''
    name = command.replace('who is' , '').strip() + ' wikipedia'
    url = next(search(name, tld="co.in", stop=1, pause=2))
    if config.WIKIURL in url:
        webbrowser.open(url)
        return 'Opening wikipedia page'
    else:
        return 'I don\'t know'


def news(command):
    '''
    Shows the news for a topic on the browser
    :param command: command received by the user
    :returns string that is said to the user
    '''
    command = nlp.remove_stopwords(command)
    topic = command.split('news')[-1].strip()
    url = config.GGLURL_NEWS
    if 'latest' in command:
        url = config.GGLURL_LATESTNEWS
    if 'today' in command:
        url = config.GGLURL_TODAYNEWS
    if topic != '':
        url = f'{url}+{topic}'
    webbrowser.open(url)
    return 'Opening in your browser'


def openw(command):
    '''
    Opens a website on the browser
    :param command: command received by the user
    :returns string that is said to the user
    '''
    command = command.replace('open' , '').strip()
    url = next(search(command, tld="co.in", stop=1, pause=2))
    webbrowser.open(url)
    return 'Opening in your browser'