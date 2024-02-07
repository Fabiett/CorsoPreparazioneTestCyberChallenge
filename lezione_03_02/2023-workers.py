# https://cyberchallenge.it/media/public/training/2023-workers.pdf

from argparse import ArgumentParser
from os.path import exists

# Creazione di un parser per gli argomenti della riga di comando
argps = ArgumentParser()
argps.add_argument('input', help='Input file')

# Estrazione del nome del file di input dagli argomenti della riga di comando
filename = argps.parse_args().input

# Verifica dell'esistenza del file di input
if not exists(filename):
    print('File not found')
    exit()

# Lettura del file di input e rimozione degli spazi bianchi iniziali e finali da ogni riga
with open(filename) as f:
    lines = [l.strip() for l in f.readlines()]

def minimum_workers(N, T, tasks):
    # Calcolo del tempo totale necessario per eseguire tutti i task
    total_time = sum(tasks)
    workers = 1

    # Ciclo fino a quando il numero di lavoratori non supera il numero massimo di lavoratori
    while workers <= N:
        # Calcolo del tempo totale utilizzato nei turni precedenti
        rounds_needed = (workers - 1) * T
        # Calcolo del tempo rimanente per l'ultimo lavoratore nel turno corrente
        time_for_last_worker = max(0, total_time - rounds_needed)

        # Se il tempo rimanente per l'ultimo lavoratore è minore o uguale al tempo massimo per turno,
        # allora il numero corrente di lavoratori è sufficiente
        if time_for_last_worker <= T:
            return workers
        
        workers += 1

    return workers

# Estrazione del numero di lavoratori e del tempo massimo per turno dalla prima riga del file di input
(n, t) = map(int, lines[0].split(' '))
# Estrazione dei tempi dei task dalla seconda riga del file di input
tasks = list(map(int, lines[1].split(' ')))

# Calcolo del numero minimo di lavoratori necessari per eseguire tutti i task entro il tempo massimo per turno
result = minimum_workers(n, t, tasks)
print(result)