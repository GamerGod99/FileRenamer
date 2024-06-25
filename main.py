import os

from scripts import *

if __name__ == "__main__":
    path = input('enter folder directory: ')

    pos = input('Enter cut positions: ').split()
    pos = tuple([int(num) for num in pos])

    cut_names(path, pos)
