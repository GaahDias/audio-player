import player
import audio
import util

import threading

import random
from colorama import Fore, Back

def main():
    util.clear_console()
    draw_ascii()

    # gives the user an input option
    print("Welcome to Audio Player! Press:\n")
    print("1 - Insert file")
    print("2 - Help")
    print("\nOption: ", end='')

    option = input()

    # print something accordingly to user input
    if option == '1':
        util.clear_console()
        draw_ascii()

        print("Insert file path: ", end='')
        path = input()
        audio_name = util.get_file_name(path)

        # initializing threads for audio and player
        t1 = threading.Thread(name='PlayerThread', target=player.start_player, args=(audio_name,))
        t2 = threading.Thread(name='AudioThread', target=audio.start_audio, args=(path,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    elif option == '2':
        util.clear_console()
        draw_ascii()

        print("Audio Player is a simple Python application for listening to audio in the console.\n")
        print("You can operate the player using these commands:\n⸰ Ctrl + Space for pausing,\n⸰ Ctrl + Arrows left and right for skipping 10 seconds in the audio (TO DO),\n⸰ Ctrl + Arrows up and down for changing the volume.\n")
        print("Press Enter to go back. ")
        tmp = input()
        main()
    else:
        main()

# Draw ascii in different colors
def draw_ascii():
    num = random.randint(0, 6)

    color_dict = {
        0: Fore.CYAN,
        1: Fore.RED,
        2: Fore.GREEN,
        3: Fore.BLUE,
        4: Fore.MAGENTA,
        5: Fore.YELLOW,
        6: Fore.WHITE,
    }

    for key, value in color_dict.items():
        if num == key:
            print(value + "\n\n")
    print(" _____  _   _  ___    _  _____     ___    _      _____  _     _  ___    ___   ")
    print("(  _  )( ) ( )(  _`\ (_)(  _  )   (  _`\ ( )    (  _  )( )   ( )(  _`\ |  _`\ ")
    print("| (_) || | | || | ) || || ( ) |   | |_) )| |    | (_) |`\`\_/'/'| (_(_)| (_) )")
    print("|  _  || | | || | | )| || | | |   | ,__/'| |  _ |  _  |  `\ /'  |  _)_ | ,  / ")
    print("| | | || (_) || |_) || || (_) |   | |    | |_( )| | | |   | |   | (_( )| |\ \ ")
    print("(_) (_)(_____)(____/'(_)(_____)   (_)    (____/'(_) (_)   (_)   (____/'(_) (_)")
    print(Fore.RESET + "\n\n")


if __name__ == "__main__":
    main()
