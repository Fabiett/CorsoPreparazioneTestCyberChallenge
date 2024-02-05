# https://cyberchallenge.it/media/public/training/2019-reverse.pdf

from argparse import ArgumentParser
from os.path import exists, isfile

# --- Gestione degli argomenti di linea di comando ---

# Creazione di un oggetto ArgumentParser per gestire gli argomenti di linea di comando
argsp = ArgumentParser()

# Aggiunta di un argomento 'input' per specificare il file di input
argsp.add_argument('input', help='input file')

# Parsing degli argomenti di linea di comando e ottenimento del nome del file di input
filename = argsp.parse_args().input

# --- Verifica dell'esistenza e del tipo del file di input ---

# Verifica se il file specificato esiste e se è effettivamente un file
if not exists(filename) and not isfile(filename):
    print('Non è un file')
    exit(1)

# --- Lettura del file di input ---

# Apre il file e legge le linee, rimuovendo gli spazi in eccesso
with open(filename, 'r') as f:
    lines = list(map(lambda l: l.strip(), f.readlines()))

# --- Elaborazione dei dati nel file di input ---

# Estrazione del numero dalla prima riga del file
n = int(lines[0])

# Estrazione del messaggio dalla seconda riga del file
msg = lines[1]

# Creazione di un insieme di caratteri unici presenti nel messaggio
chrs = set(msg)

# Creazione di un dizionario contenente la frequenza di ciascun carattere nel messaggio
frqcnt_bkp = {c: msg.count(c) for c in chrs}

# Creazione di un nuovo dizionario per la frequenza dei caratteri
frqcnt = dict()

# Iterazione attraverso i caratteri unici nel messaggio
for c in chrs:
    # Conta il numero di occorrenze del carattere nel messaggio
    cnt = msg.count(c)
    
    # Recupera la lista dei caratteri con la stessa frequenza dal dizionario frqcnt
    prv = frqcnt.get(cnt, [])
    
    # Aggiorna il dizionario frqcnt con il carattere corrente
    frqcnt[cnt] = prv + [c]

# Ordina i caratteri con la stessa frequenza come descritto nel PDF
for k, v in frqcnt.items():
    frqcnt[k] = sorted(v)

# --- Stampa del risultato elaborato ---

# Stampa dei caratteri invertiti in base alla frequenza
list( # map da sola non esegue i passaggi, ma aspetta di essere chiamata
    map( # preparo la funzione che mi aiuterà a modificare i caratteri
        lambda c: # funzione anonima che mi serve per sostituire i caratteri. prende in input il carattere attuale
            print(
                # modifico la stringa in modo che il carattere attuale sia sostituito con il carattere -(n-esimo) con la stessa frequenza
                (tmp:=frqcnt[frqcnt_bkp[c]])[::-1][tmp.index(c)], 
                end='' # evito che mi stampi un \n a fine riga
            ),
        msg
    )
)

# Stampa di una nuova linea per separare l'output
print()
