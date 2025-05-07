import pandas as pd 
from datetime import datetime

# Fichier CSV à utiliser
CSV_FILE="history_wator_groupe1.csv" 

def save_results(chronons :int, num_fishes :int, num_sharks :int) -> None:
    """
        Sauvegarde les résultats de la simulation dans le fichier CSV: history_wator_groupe1.csv.

        Cette fonction crée un DataFrame contenant la date, l'heure, le nombre de chronons,
        le nombre de poissons et le nombre de requins, puis l'enregistre dans le fichier CSV.

        Args:
            chronons (int): Le nombre de chronons écoulés dans la simulation.
            num_fishes (int): Le nombre de poissons présents à la fin de la simulation.
            num_sharks (int): Le nombre de requins présents à la fin de la simulation.
    """
    # Création d'un dictionnaire à partir de résultats 
    results={
        "Date": [datetime.now().date().strftime("%d/%m/%y")],
        "Heure_Minutes": [datetime.now().time().strftime("%H:%M")],
        "Chronons": [chronons], 
        "Nombre_Poissons": [num_fishes],
        "Nombre_Requins": [num_sharks]
    }
    
    # Création du dataFrame à partir du dictionnaire 
    data_save = pd.DataFrame(results)

    # Enregistrement des résultats dans le fichier CSV
    # Le mode "a" permet d'ajouter les nouvelles données à la fin du fichier existant
    # L'argument header est défini pour écrire l'en-tête uniquement si le fichier n'existe pas encore
    data_save.to_csv(CSV_FILE, mode="a", header=not pd.io.common.file_exists(CSV_FILE), index=False) 