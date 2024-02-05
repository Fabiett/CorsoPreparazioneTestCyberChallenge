# https://cyberchallenge.it/media/public/training/2021-unbalancer.pdf

from argparse import ArgumentParser
from os.path import exists

# --- Gestione degli argomenti di linea di comando ---

# Creazione di un oggetto ArgumentParser per gestire gli argomenti di linea di comando
argsp = ArgumentParser()
# Aggiunta di un argomento 'input' per specificare il file di input
argsp.add_argument('input', help='Input file')
# Parsing degli argomenti di linea di comando e ottenimento del nome del file di input
filename = argsp.parse_args().input

# --- Verifica dell'esistenza e del file di input ---

# Verifica se il file specificato esiste
if not exists(filename):
    print('File not found')
    exit(1)

# --- Lettura del file di input ---
with open(filename) as f:
    lines = [l.strip() for l in f.readlines()]

# --- Elaborazione dei dati nel file di input ---

# Estrazione del numero di workers e dei movimenti disponibili
workers, available_movements = [int(n) for n in lines[0].split(' ')]
# Estrazione dei task
tasks = [int(n) for n in lines[1].split(' ')]
# Ordina il numero dei task in ordine decrescente
tasks = sorted(tasks, reverse=True)

# Calcola la massima differenza raggruppando i primi 'available_movements' task
print(sum(tasks[:available_movements+1]))
