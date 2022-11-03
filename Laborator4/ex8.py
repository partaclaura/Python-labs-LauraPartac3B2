# Să se scrie o funcție ce primește un parametru cu numele dir_path.
# Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor
# aflate în rădăcina directorului dir_path.
# Exemplu apel funcție: functie("C:\\director")
# va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
# Calea "C:\\director" are pe disc următoarea structură:
# C:\\director\\fisier1.txt <- fișier
# C:\\director\\fisier2.txt <- fișier
# C:\\director\\director1 <- director
# C:\\director\\director2 <- director


import os


def files_in_dir(dir_path):
    return [os.path.abspath(file) for file in os.scandir(dir_path) if os.path.isfile(file)]


path = "C:\\Python-labs\\files"
print(files_in_dir(path))
