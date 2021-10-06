import speech_recognition as sr
import pyttsx3
import languageprocessing as nlp
import browser
import clock
from volume import volume
import operations as op


class Alexa:
    
    
    def __init__(self):
        '''
        Text to sppech and speech to text objects are created
        '''
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.say('Hi, I am Alexa.')
    
    
    def say(self, text):
        '''
        Output for the virual assistant
        :param text: string text that the virtual assistant says to the user
        '''
        engine = self.engine
        print('Alexa: ' + text)
        engine.say(text)
        engine.runAndWait()
    
    
    def ask_user(self):
        '''
        Input for the virtual assistant
        :returns string text that the user says to the virtual assistant
        '''
        r = self.r
        try:
            with sr.Microphone() as source:
                self.say('How can I help you?')
                voice = r.listen(source)
                command = r.recognize_google(voice)
                print('Me: ' + command)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '').strip()
        except:
            return ''
        return command
    
    
    def run(self):
        '''
        Processing of the virtual assistant
        '''
        command = self.ask_user()
        say = self.say
        if 'play' in nlp.lemmatize(command):
            say(browser.play_song(command))
        elif 'search' in command:
            say(browser.searchw(command))
        elif 'who is' in command:
            say(browser.who_is(command))
        elif 'news' in command:
            say(browser.news(command))
        elif 'open' in command:
            say(browser.openw(command))
        elif op.check(command):
            say(op.reply(command))
            self.run()
        elif 'joke' in command:
            say(op.jokes())
        elif 'weather' in command or 'temperature' in command:
            say(op.weather(command))
        elif 'time' in command:
            say(clock.time(command))
        elif 'date' in command or 'day' in command:
            say(clock.date())
        elif 'volume' in nlp.lemmatize(command) \
            or 'mute' in nlp.lemmatize(command):
            say(volume(command))
        else:
            say('I could not hear you properly')


''' Driver Code '''
if __name__ == '__main__':
    alexa = Alexa()
    alexa.run()