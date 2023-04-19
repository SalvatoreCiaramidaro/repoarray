import numpy as np

# Apri il file contenente i voti degli studenti in modalità lettura
with open("voti2.txt", "r") as file_voti:
    
    # Inizializza la somma dei voti a 0
    somma_voti = 0
    
    # Inizializza il contatore degli studenti a 0
    num_studenti = 0
    
    # Leggi il file riga per riga
    for linea in file_voti:
        
        # Converte la riga in un array formata da numeri interi
        voti_studente = np.fromstring(linea, sep=' ')
        print(voti_studente)
        
        # Aggiungi i voti dello studente alla somma
        somma_voti += np.sum(voti_studente)
        
        # Incrementa il contatore degli studenti
        num_studenti += 1
    
    # Calcola la media dei voti
    media_voti = somma_voti / (num_studenti * voti_studente.size)
    
    # Stampa la media dei voti a video
    print(f'La media dei voti di {num_studenti} studenti è: {media_voti}')
