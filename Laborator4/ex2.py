# Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie
# scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul
# directorului de la calea folder, ce incepe cu litera A.

import os


def a_files(directory, file):
    fd = open(file, "wt")
    for root, _, files in os.walk(os.path.abspath(directory)):
        for f in files:
            if f.startswith("A"):
                fd.write(os.path.join(root, f) + os.linesep)


directory_path = "C:\\Python-labs\\files"
a_files(directory_path, "C:\\Python-labs\\a_files.txt")
