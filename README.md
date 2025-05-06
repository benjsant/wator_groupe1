# Wator_Groupe1
une simulation de dynamique de population avec des requins et des poissons codé en python

## Description du projet 

Ce projet a été réalisé par [Aurelien](https://github.com/Aurelien-L), [Benjamin](https://github.com/benjsant) et [Sayana](https://github.com/sayana-project) lors de la formation Dev IA chez Simplon HDF-Lille. L'objectif est de créer une simulation (Wa-Tor) utilisant le langage de programmation Python, avec une interface graphique développée en PyQt5.

- Pour en savoir plus sur la simulation Wa-Tor, consultez [cette page Wikipedia](https://en.wikipedia.org/wiki/Wa-Tor).

## Arborescence du projet 

Voici l'aborescence du projet pour mieux localiser certains fichiers : 

- **interface/** : Dossier contenant les fichiers liés à l'interface utilisateur.
  - **`__init__.py`** : Fichier d'initialisation du module.
  - **grid_view.py** : Fichier pour la vue de la grille.
  - **main_window.py** : Fichier pour la fenêtre principale de l'application.
  - **history_window.py**: Fichier pour le tableau d'historique des simulations. 
- **entity/** : Dossier contenant les entités du projet.
  - **`__init__.py`** : Fichier d'initialisation du module.
  - **fish.py** : Fichier pour la classe représentant le poisson.
  - **shark.py** : Fichier pour la classe représentant le requin.
  - **clown_fish.py**:Fichier pour la sous-classe de poisson représentant le poisson tropical.  
- **uils/** : Dossier contenant des utilitaires.
  - **config.py** : Fichier de configuration.
  - **data-management.py**: Fichier pour la gestion de donnée, principalement la sauvegarde des simulations passé .
- **main.py** : Point d'entrée de l'application.
- **planet.py** : Fichier pour la classe représentant une planète.
- **README.md** : Documentation du projet.
- **history_wator_groupe1.csv** : Fichier CSV de sauvegarde des simulations précédentes. 

## Utilisation du projet 

### Pré-requis et installation 

1. **Cloner le projet** : Pour utiliser l'application, clonez le projet depuis GitHub en [cliquant ici](https://github.com/benjsant/wator_groupe1.git).

   Vous pouvez également exécuter la commande suivante si vous avez **Git** installé sur votre machine :

```bash
git clone https://github.com/benjsant/wator_groupe1.git
```

2. **Installer Python** : Assurez-vous d'avoir Python 3.13.3 installé sur votre machine. Utilisez un terminal de commande pour lancer la simulation. 
   
3. **Installer les dépendances**: Assurez-vous également d'installer les paquets Python suivants avec la commande pip: 
  
```bash
pip install -r requirements.txt
```

