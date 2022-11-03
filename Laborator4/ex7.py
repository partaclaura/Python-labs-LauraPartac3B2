# Să se scrie o funcție care primește ca parametru un șir de caractere
# care reprezintă calea către un fișer si returnează un dicționar cu
# următoarele cămpuri: full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False
# daca se poate citi din/scrie in fisier.


import os


def file_info(file_path):
    info = {'full_path': os.path.abspath(file_path), 'file_size': os.path.getsize(file_path)}
    f = os.path.split(file_path)[1].split('.')
    info['file_extension'] = f[1] if len(f) > 1 else ""
    info['can_read'] = os.access(file_path, os.R_OK)
    info['can_write'] = os.access(file_path, os.W_OK)
    return info


path = "C:\\Python-labs\\files\\main.py"
print(file_info(path))
