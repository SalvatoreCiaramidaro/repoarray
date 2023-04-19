import numpy as np

# Apri il file contenente i voti degli studenti in modalità lettura
with open("voti.txt", "r") as file_voti:
    
    # Leggi i voti dal file e convertili in un array Numpy
    voti = np.loadtxt(file_voti)
    print(voti)
    
    # Calcola la media dei voti degli studenti
    media_voti = np.mean(voti)
    
    # Stampa la media dei voti a schermo
    print("La media dei voti degli studenti è:", media_voti)
