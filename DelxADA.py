import os
import datetime

# Percorso della cartella da pulire
directory = r'C:\xADABackup'

# Calcola la data di soglia: tutti i file più vecchi di questa data verranno eliminati
# Vers.1.10 I giorni di cancellazione non sono più fissi ma selezionabili dall'utente (variabile giorni)

giorni = int(input("\033[41m\033[97mInserisci il numero di giorni per la soglia di cancellazione: \033[0m"))

soglia = datetime.datetime.now() - datetime.timedelta(days=giorni) # variabile giorni

def elimina_vecchi_files(cartella):
    for root, dirs, files in os.walk(cartella, topdown=False):
        # Elimina i file più vecchi della soglia
        for name in files:
            try:
                filepath = os.path.join(root, name)
                filetime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                if filetime < soglia:
                    os.remove(filepath)
                    print(f"Eliminato file: {filepath}")
            except Exception as e:
                print(f"Errore nell'eliminare il file {name}: {e}")
        
        # Dopo aver eliminato i file, prova a eliminare le cartelle (se sono vuote)
        for name in dirs:
            try:
                dirpath = os.path.join(root, name)
                if not os.listdir(dirpath):  # Controlla se la cartella è vuota
                    os.rmdir(dirpath)
                    print(f"Eliminata cartella vuota: {dirpath}")
            except Exception as e:
                print(f"Errore nell'eliminare la cartella {name}: {e}")

# Esegui la funzione di pulizia
# print ("___ELIMINAZIONE FILE xADABackup___")
print("\033[42m\033[97m___ELIMINAZIONE FILE xADABackup___\033[0m")
print ()
print(f"\033[42m\033[97mVerranno eliminati i file più vecchi di {giorni} giorni\033[0m")
print ()
elimina_vecchi_files(directory)
