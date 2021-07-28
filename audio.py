from pygame import mixer
from pydub import AudioSegment

import util
import main

from time import sleep
import os

def start_audio(path):
    # check if all the steps are sucessfull
    try:
        mixer.init()
        clear_audio_cache()
        convert_audio(path)

        mixer.music.load("cache/audio.wav")
        mixer.music.set_volume(0.8)
        mixer.music.play()
    # if not, prints an error message and go back to menu
    except Exception as err:
        util.clear_console()
        print(f"Something went wrong... Error: {err}")

        for i in range(5, 0, -1):
            print(f"Returning to menu in {i}...", end="\r")
            sleep(1)
        main.main()
        
# creates cache folder, and converts audio format to wav
def convert_audio(path):
    file = util.get_file_name(path)
    ext = file.split('.')[1]

    if not os.path.isdir('cache'):
        os.system('mkdir cache')

    AudioSegment.from_file(path, format=ext).export('cache/audio.wav', format='wav')

# removes audio from cache folder
def clear_audio_cache():
    cache_path = 'cache/audio.wav'

    if os.path.isfile(cache_path):
        os.system('rm ' + cache_path)

def play_pause_audio():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()

def set_audio_volume(db):
    current_volume = mixer.music.get_volume()

    if current_volume < 1 and current_volume > 0 or db <= 1 and db >= 0:
        mixer.music.set_volume(db)

def stop_audio():
    mixer.music.stop()
    clear_audio_cache()

if __name__ == "__main__":
    util.clear_console()
    print("Please, start the main.py file!")