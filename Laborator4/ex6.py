# Să se scrie o funcție care are același comportament ca funcția de la 
# exercițiul anterior, cu diferența că primește un parametru în plus: 
# o funcție callback, care primește un parametru, iar pentru fiecare 
# eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca 
# parametru.


import os


def handle_exceptions(exception, exception_message):
    try:
        raise exception(exception_message)
    except exception as e:
        print("Error:", e)


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


def ex6(target, to_search, error_function):
    if os.path.isfile(to_search):
        if search_in_file(target, to_search):
            print("Found target in given file!")
        else:
            print("Target not in given file!")
    elif os.path.isdir(to_search):
        print(search_in_dir(target, to_search))
    else:
        error_function(ValueError, "not file or directory")


message = "hello"
directory_path = "C:\\Python-lab"
ex6(message, directory_path, handle_exceptions)
