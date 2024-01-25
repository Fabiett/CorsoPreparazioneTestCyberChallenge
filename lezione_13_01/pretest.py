# Apertura del file, lettura e salvataggio su variabile dei dati
with open("input.txt") as fp:
  input_esercizio = fp.read() 

# Print del contenuto della variabile
print(input_esercizio)

# Divisione delle stringhe per il carattere new line
righe_input = input_esercizio.split('\n')

# Assegnazione delle variabili giuste
info_esercizio = righe_input[0]
risposte_corrette = righe_input[1]
risposte_classe = righe_input[2:] # List splicing ;)

# Print delle risposte date dagli alunni
print(risposte_classe)

# Inizializzazione counter esterno
counter_risposte = 0

# Preparazione variabile risultati
punteggi_classe = []

while(counter_risposte < len(risposte_classe)): # Ciclo che scorre per tutte le risposte della classe
    
    punteggio_studente = 0

    # Variabile temporanea, non necessaria, ma utile per tenere traccia di ciò che ci interessa
    risposte_studente = risposte_classe[counter_risposte]

    # Inizializzazione counter interno
    counter_stringa = 0

    while(counter_stringa < len(risposte_corrette)): # Ciclo che scorre per ogni carattere della stringa
        if(risposte_corrette[counter_stringa] == risposte_studente[counter_stringa]):
            punteggio_studente += 1
        counter_stringa += 1 # Incremento del counter interno
 
    # Accumulazione dei risultati in una lista come stringhe
    punteggi_classe.append(str(punteggio_studente)) 
    
    # Incremento del counter esterno
    counter_risposte += 1

# Unione finale dei risultati in una singola stringa
output = "\n".join(punteggi_classe)

# Print del risultato finale
print(output)

# Controllo del risultato ufficiale con quello ottenuto dalla nostra soluzione
with open("output.txt") as fp:
    output_corretto = fp.read().strip()

if output_corretto == output: print("Amesso a CyberChallenge.it '24!!!")