# Să se scrie o funcție ce primeste un singur parametru, director,
# ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator
# (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’

import os


def unique_ext(directory):
    extensions = []
    for file in os.listdir(directory):
        split_filename = file.split('.')
        if split_filename[1] not in extensions:
            extensions.append(split_filename[1])
    extensions.sort()
    return ' '.join(extensions)


directory_path = "C:\\Python-labs"
print(unique_ext(directory_path))
