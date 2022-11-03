# Să se scrie o funcție care primește ca argumente două șiruri de
# caractere, target și to_search și returneaza o listă de fișiere
# care conțin to_search. Fișierele se vor căuta astfel: dacă target
# este un fișier, se caută doar in fișierul respectiv iar dacă este
# un director se va căuta recursiv in toate fișierele din acel director.
# Dacă target nu este nici fișier, nici director, se va arunca o excepție
# de tipul ValueError cu un mesaj corespunzator.


import os


def search_in_file(string_to_search, file):
    with open(file, 'r') as f:
        if string_to_search in f.read():
            return True
        else:
            return False


def search_in_dir(string_to_search, directory):
    found = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if search_in_file(string_to_search, os.path.join(root, filename)):
                found.append(filename)
    return found


def ex5(target, to_search):
    try:
        if os.path.isfile(to_search):
            if search_in_file(target, to_search):
                print("Found target in given file!")
            else:
                print("Target not in given file!")
        elif os.path.isdir(to_search):
            print(search_in_dir(target, to_search))
        else:
            raise ValueError("not file or directory")
    except ValueError as e:
        print("ValueError:", e)


message = "hello"
directory_path = "C:\\Python-labs"
ex5(message, directory_path)
