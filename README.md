Speedrun le Casse-Brique
Présentation du jeu
Speedrun le Casse-Brique est un jeu d'arcade réalisé en Python avec Pygame et NumPy.

Le principe est simple : déplacer une raquette pour faire rebondir une balle et détruire toutes les briques à l'écran. Le jeu encourage la rapidité : plus une brique est détruite tôt, plus elle rapporte de points.
Règles du jeu
- La partie commence avec 48 briques, réparties en 6 lignes et 8 colonnes.
- La balle est initialement attachée à la raquette. Il faut la lancer pour commencer à jouer.
- La balle rebondit sur les murs, la raquette et les briques.
- Chaque brique détruite rapporte 100 points minimum, auxquels s'ajoute un bonus qui diminue avec le temps.
- La partie est gagnée lorsque les 48 briques ont été détruites.
- La partie est perdue si la balle atteint le bas de la zone de jeu.
- À la fin de la partie, le score final est affiché et il est possible de revenir au menu principal.
Commandes
Touche	Action
Entrée	Démarrer une partie depuis le menu principal
Q	Déplacer la raquette vers la gauche
D	Déplacer la raquette vers la droite
Espace	Lancer la balle au début de la partie
Espace	Retourner au menu après la fin de la partie
Fermer la fenêtre	Quitter le jeu


Les commandes Q et D sont adaptées à un clavier AZERTY.

Prérequis
- Python 3
- Les bibliothèques pygame et numpy
Installation
1. Télécharger ou cloner le projet, puis ouvrir un terminal dans son dossier.

2. (Recommandé) Créer et activer un environnement virtuel :
   macOS / Linux :
   python3 -m venv .venv
   source .venv/bin/activate
   Windows (PowerShell) :
   py -m venv .venv
   .venv\Scripts\Activate.ps1
3. Installer les dépendances :
   python -m pip install pygame numpy
Lancement du jeu
Depuis le dossier contenant le fichier jeu.py, exécuter :
python jeu.py
Selon la configuration, la commande peut être python3 jeu.py sur macOS/Linux ou py jeu.py sur Windows. Si le fichier Python porte un autre nom, adapter la commande.

Une fenêtre s'ouvre sur le menu du jeu. Appuyer sur Entrée, puis sur Espace pour lancer la balle.
Fonctionnement technique
- Pygame gère l'affichage, les déplacements, les collisions et les commandes clavier.
- NumPy représente les briques avec une matrice de 6 × 8 et permet de compter les briques restantes.
- Le jeu fonctionne à une cadence maximale de 60 FPS.
- L'affichage utilise une résolution interne de 320 × 180 pixels, agrandie dans une fenêtre de 1280 × 720 pixels.
- Le jeu suit plusieurs états : menu, initialisation, partie et fin de partie.


# Membres de l'équipe : 
`- Rudy`
`- Megan`
`- Saleh`