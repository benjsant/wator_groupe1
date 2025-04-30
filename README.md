# Wator_Groupe1
une simulation de dynamique de population avec des requins et des poissons codé en python

## Description du projet 

Ce projet a été réalisé par [Aurelien](https://github.com/Aurelien-L), [Benjamin](https://github.com/benjsant) et [Sayana](https://github.com/sayana-project) lors de la formation Dev IA chez Simplon HDF-Lille. 
Le but est de crée une simulation (Wa-Tor) utilisant le langage de programmation Python avec l'interface graphique PyQt5. 


- [Explication de la simulation Wa-Tor](https://en.wikipedia.org/wiki/Wa-Tor)

## Arborescence du projet 

Voici une aborescence du projet pour mieux localiser certains fichier 

- **interface/** : Dossier contenant les fichiers liés à l'interface utilisateur.
  - **`__init__.py`** : Fichier d'initialisation du module.
  - **grid_view.py** : Fichier pour la vue de la grille.
  - **main_window.py** : Fichier pour la fenêtre principale de l'application.
  
- **entity/** : Dossier contenant les entités du projet.
  - **`__init__.py`** : Fichier d'initialisation du module.
  - **fish.py** : Fichier pour la classe représentant le poisson.
  - **shark.py** : Fichier pour la classe représentant le requin.
  
- **uils/** : Dossier contenant des utilitaires.
  - **config.py** : Fichier de configuration.

- **main.py** : Point d'entrée de l'application.
- **planet.py** : Fichier pour la classe représentant une planète.
- **README.md** : Documentation du projet.


## Utilisation du projet 

### Pré-requis et installation 

- Pour utiliser l'application, il suffit de cloner le projet depuis le Lien GitHub en [Cliquant ici](https://github.com/benjsant/wator_groupe1.git) ; 

Vous pouvez également lancé la commande ci-dessous si vous avez **Git installé sur votre machine** : 

```
git clone https://github.com/benjsant/wator_groupe1.git
```

- Il faut également avoir installé Python sur sa machine ( utiliser un terminal de commande pour lancer la simulation) ;

- Installer et importer les paquets python **pip** suivant: **PyQt5, pandas**, vous pouvez les installez en copiant les lignes suivantes dans votre terminal python:

```
pip install PyQt5 
pip install pandas
```

