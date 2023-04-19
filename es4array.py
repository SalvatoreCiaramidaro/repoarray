import numpy as np

# Apri il file contenente i cognomi degli studenti in modalità lettura
with open("cognomi.txt", "r") as file_cognomi:
    # Crea una lista con i cognomi degli studenti
    lista_cognomi = file_cognomi.read().splitlines()

# Apri il file contenente i voti degli studenti in modalità lettura
with open("voti4.txt", "r") as file_voti:
    
    # Inizializza la somma dei voti per ogni studente a 0
    somma_voti_studenti = np.zeros((len(lista_cognomi), 4))
    
    # Inizializza il contatore degli studenti a 0
    num_studenti = 0

    # Leggi il file riga per riga
    for linea in file_voti:
        
        # Converte la riga in un array di numeri interi
        voti_studente = np.fromstring(linea, sep=' ')
        
        # Aggiungi i voti dello studente alla somma dei voti degli studenti
        somma_voti_studenti[num_studenti] = voti_studente
        
        # Incrementa il contatore degli studenti
        num_studenti += 1
    
    # Calcola la media dei voti per ogni studente
    media_voti_studenti = np.mean(somma_voti_studenti, axis=1)

    # Calcola la media dei voti della classe
    media_voti_classe = np.mean(media_voti_studenti)

    # Stampa la media dei voti per ogni studente a schermo
    print("La media dei voti per ogni studente è:")
    for i in range(len(lista_cognomi)):
        print(lista_cognomi[i], ":", media_voti_studenti[i])
    
    # Stampa la media dei voti della classe a schermo
    print("La media dei voti degli studenti della classe è:", media_voti_classe)
