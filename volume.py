import config
import languageprocessing as nlp
import json
from pyautogui import press
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def volume(command):
    '''
    Manipulates the system volume
    :param command: command received by the user
    :returns string that is said to the user
    '''
    command = nlp.remove_stopwords(command)
    volume = command.split(' ')[-1]
    if volume.isnumeric():
        volume = 100 if int(volume) > 100 else int(volume)
        set_volume(volume)
        press("volumedown")
        press("volumeup")
        return 'Setting the volume to ' + str(volume)
    else:
        if 'full' in command:
            set_volume(100)
            press("volumeup")
            return 'Setting the volume to 100'
        elif 'half' in command:
            set_volume(50)
            press("volumedown")
            press("volumeup")
            return 'Setting the volume to 50'
        elif 'mute' in nlp.lemmatize(command):
            press("volumemute")
            return 'System Muted/Unmuted'
        elif 'increase' in nlp.lemmatize(command):
            press("volumeup")
            return 'Increasing the volume'
        elif 'decrease' in nlp.lemmatize(command):
            press("volumedown")
            return 'Decreasing the volume'
    return 'Couldn\'t understand'


def set_volume(volume):
    '''
    Changes the volume to the given number
    :param volume: volume in percentage
    '''
    with open(config.JSON_PATH + 'volume.json', 'r') as file:
        p2v = json.load(file)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volumedevice = cast(interface, POINTER(IAudioEndpointVolume))
    volumedevice.SetMasterVolumeLevel(p2v[str(volume)], None)