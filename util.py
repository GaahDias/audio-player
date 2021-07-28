import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_file_name(path):
    if '/' in path:
        return path.split('/')[-1]
    else:
        return path

if __name__ == "__main__":
    clear_console()
    print("Please, start the main.py file!")