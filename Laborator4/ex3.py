# Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna
# ultimele 20 de caractere din conținutul fișierului. Dacă parametrul
# reprezintă calea către un director, se va returna o listă de tuple
# (extensie, count), sortată descrescător după count, unde extensie
# reprezintă extensie de fișier, iar count - numărul de fișiere cu acea
# extensie. Lista se obține din toate fișierele (recursiv) din directorul
# dat ca parametru.

import os


def get_last20_ch(file):
    with open(file, "rb") as fd:
        return str(fd.read())[len(fd.read()) - 20:]


def get_ext_count(directory):
    ext_count = {}
    for root, directories, files in os.walk(directory):
        for filename in files:
            split_filename = filename.split('.')
            if split_filename[1] in ext_count.keys():
                ext_count[split_filename[1]] = ext_count[split_filename[1]] + 1
            else:
                ext_count[split_filename[1]] = 1
    return [(k, v) for k, v in ext_count.items()]


def ex3(my_path):
    if os.path.isdir(my_path):
        return get_ext_count(my_path)
    elif os.path.isfile(my_path):
        return get_last20_ch(my_path)


directory_path = "C:\\Python-labs\\fileExample.txt"
print(ex3(directory_path))

