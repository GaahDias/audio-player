from pynput.keyboard import Key
from pynput import keyboard

import audio
import util

import cursor

# player strings that are displayed dynamically in screen
CURRENT_AUDIO = ''
BUTTONS = (' ' * 21) + '⏮  ⏸  ⏭'
VOLUME = 'Vol.: 80%'
# volume starts at 80%
VOLUME_DB = 0.8

def draw_player():
    global CURRENT_AUDIO, AUDIO_NAME

    util.clear_console()

    bar = '━' * 50
    title = (' ' * 18) + 'AUDIO PLAYER'
    if len(CURRENT_AUDIO) > 19:
        CURRENT_AUDIO = CURRENT_AUDIO[:19] + '...'
    audio_name = (' ' * 2) + f'Playing: {CURRENT_AUDIO}'

    print(f'\n\n{title}\n\n\n{audio_name} | {VOLUME}\n{bar}\n{BUTTONS}')

# change the play/pause buttons and play/pause the audio
def play_pause():
    global BUTTONS
    
    if '⏸' in BUTTONS:
        BUTTONS = (' ' * 21) + '⏮  ⯈  ⏭'
    else:
        BUTTONS = (' ' * 21) + '⏮  ⏸  ⏭'
    
    audio.play_pause_audio()
    draw_player()

# change the volume in 10 steps
def change_volume(vol):
    global VOLUME, VOLUME_DB

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
                VOLUME = "Vol.: " + key
                VOLUME_DB = vol
                audio.set_audio_volume(vol)
    draw_player()


def start_player(audio_name):
    global CURRENT_AUDIO
    CURRENT_AUDIO = audio_name

    draw_player()
    cursor.hide()

    # listen for keys
    with keyboard.GlobalHotKeys({
            '<ctrl>+<space>': play_pause,
            '<ctrl>+<up>': lambda: change_volume(vol=VOLUME_DB+0.1),
            '<ctrl>+<down>': lambda: change_volume(vol=VOLUME_DB-0.1)}) as listener:
        listener.join()


if __name__ == "__main__":
    util.clear_console()
    print("Please, start the main.py file!")