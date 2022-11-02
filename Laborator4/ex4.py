# Să se scrie o funcție ce returnează o listă cu extensiile unice a
# fișierelor din directorul dat ca argument la linia de comandă (nerecursiv).
# Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are
# extensie, deci nu va apărea în lista finală.

import os


def unique_ext(directory):
    extensions = []
    for file in os.scandir(directory):
        if file.is_file():
            split_filename = file.name.split('.')
            if split_filename[1] not in extensions:
                extensions.append(split_filename[1])
            else:
                extensions.remove(split_filename[1])
    extensions.sort()
    return ' '.join(extensions)


directory_path = "C:\\Python-labs\\files"
print(unique_ext(directory_path))

