from scripts import *
from mp3_scripts import *

if __name__ == "__main__":

    action = input('Enter which action to use: ')

    if action == '0':
        path = input('enter folder directory: ')

        pos = input('Enter cut positions: ').split()
        pos = tuple([int(num) for num in pos])

        cut_names(path, pos)

    elif action == '1':
        path = input('enter folder directory: ')

        title_to_filename(path)

    elif action == '2':
        path = input('enter folder directory: ')

        enum_files(path)
