import pygame
import numpy as np

# Initialisation de Pygame
pygame.init()

# Résolution interne (virtuelle)
LARGEUR_INTERNE = 320
HAUTEUR_INTERNE = 180

# Résolution réelle de la fenêtre affichée sur l'écran
LARGEUR_FENETRE = 1280
HAUTEUR_FENETRE = 720

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Jeu - py game")

# Création de la surface
canvas = pygame.Surface((LARGEUR_INTERNE, HAUTEUR_INTERNE), pygame.SRCALPHA)

# Horloge pour limiter la vitesse du jeu (60 FPS)
clock = pygame.time.Clock()
delta = 0.0

# Police d'écriture
police = pygame.font.SysFont("Arial", 16)

# Variables
en_cours = True

# Fonctions


# Game loop
while en_cours:
    # -----------------------------------
    # --- Update --- évènements ponctuels
    # -----------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # --------------
    # --- Update ---
    # --------------
    input_joueur = pygame.key.get_pressed()


    # ------------
    # --- Draw ---
    # ------------
    # On vide l'écran pour le remplir d'une couleur unie RVB
    canvas.fill((30, 30, 50))

    # Dessin rectangle pour test
    pygame.draw.rect(canvas, (255, 0, 0), (50, 50, 40, 20))

    # redimensionne et dessine de la surface (à l'échelle) sur la fenêtre + MAJ afficahge jeu
    canvas_redimensionne = pygame.transform.scale(canvas, (LARGEUR_FENETRE, HAUTEUR_FENETRE))
    fenetre.blit(canvas_redimensionne, (0, 0))
    pygame.display.flip()

    # Régler les images par seconde à 60
    delta = clock.tick(60) / 1000.0

# Fin du programme
pygame.quit()