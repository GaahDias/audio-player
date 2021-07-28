from pynput.keyboard import Key
from pynput import keyboard

import audio
import util

import cursor

current_audio = ''
buttons = (' ' * 21) + '⏮  ⏸  ⏭'
volume = 'Vol.: 80%'

volume_db = 0.8

def draw_player():
    global current_audio

    util.clear_console()

    if len(current_audio) > 19:
        current_audio = current_audio[:19] + '...'

    title = (' ' * 18) + 'AUDIO PLAYER'
    audio_name = (' ' * 2) + f'Playing: {current_audio}'
    bar = '━' * 50

    print(f'\n\n{title}\n\n\n{audio_name} | {volume}\n{bar}\n{buttons}')
    cursor.hide()

# change the play/pause buttons and play/pause the audio
def play_pause():
    global buttons
    
    if '⏸' in buttons:
        buttons = (' ' * 21) + '⏮  ⯈  ⏭'
    else:
        buttons = (' ' * 21) + '⏮  ⏸  ⏭'
    
    audio.play_pause_audio()
    draw_player()

# change the volume in 10 steps
def change_volume(vol):
    global volume
    global volume_db

    volume_dict = {
        "100%": 1,
        "90%": 0.9,
        "80%": 0.8,
        "70%": 0.7,
        "60%": 0.6,
        "50%": 0.5,
        "40%": 0.4,
        "30%": 0.3,
        "20%": 0.2,
        "10%": 0.1,
        "0%": 0
    }
    if vol <= 1 and vol >= 0:
        for key, value in volume_dict.items():
            if round(vol,1) == value:
                volume = "Vol.: " + key
                volume_db = vol
                audio.set_audio_volume(vol)
    draw_player()


def start_player(audio_name):
    global current_audio
    current_audio = audio_name

    draw_player()

    # listen for keys
    with keyboard.GlobalHotKeys({
            '<ctrl>+<space>': play_pause,
            '<ctrl>+<up>': lambda: change_volume(vol=volume_db+0.1),
            '<ctrl>+<down>': lambda: change_volume(vol=volume_db-0.1)}) as listener:
        listener.join()


if __name__ == "__main__":
    print("Please, start the main.py file!")