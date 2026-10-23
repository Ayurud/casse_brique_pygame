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
pygame.display.set_caption("Test - py game")

# Création de la surface
canvas = pygame.Surface((LARGEUR_INTERNE, HAUTEUR_INTERNE), pygame.SRCALPHA)

# Horloge pour limiter la vitesse du jeu (60 FPS)
clock = pygame.time.Clock()
delta = 0.0

# Police d'écriture
police = pygame.font.SysFont("Arial", 16)

# Variables
en_cours = True

score = 0.0                 # Score du joueur durant la partie, initialisé à 0
min_score = 100.0           # Valeur minimale d'une brique quand détruite
bonus_score = 900.0         # Bonus se rajoutant à la valeur d'une brique, il diminue dans le temps (+vite = +de score)
game_over = False           # Condition de gameover
tableau_fini = False        # Indicateur permetant d'indiquer que le "gameover" est initié par le nettoyage complet des briques

raquette = pygame.Rect(140, 160, 25, 4)     # Raquette du joueur
raquette_x_float = float(raquette.x)        # On récupère le x en float pour la partie update
vitesse_raquette = 130.0                    # Vitesse de la raquette

scotch = True
balle = pygame.Rect(raquette.centerx - 2, raquette.y - 4 - 1, 4, 4) # Balle au milieu et 1 px au dessus, elle a une taille de 4x4
balle_x_float = float(balle.x)  # On récupère le x en float pour la partie update
balle_y_float = float(balle.y)  # On récupère le y en float pour la partie update
vitesse_balle = 100.0           # Vitesse de la balle
direction_balle = [0.0, 0.0]    # Vecteur de direction de la balle, x et y

matrice_briques = np.ones((6, 8), dtype=int) # Matrice des briques avec initialisation
brique_reference = pygame.Rect(0, 0, 23, 8)  # Dimensions de référence d'une brique
briques_restantes = np.sum(matrice_briques)  # Compteur de briques restantes

statuts_jeu = ["menu", "init", "jeu", "gameover"]   # Tous les états possible du jeu
statut_en_cours = 0                                 # Etat du jeu en cours, le code exécuté dans la gameloop ne sera pas le même selon le statut

# Fonctions
def afficher_texte(texte, x, y):
    """
    Fonction permettant d'afficher du texte à l'écran aux coordonnées x et y
    """
    surface_texte = police.render(str(texte), False, (255, 255, 255))
    canvas.blit(surface_texte, (x, y))

def statut_suivant():
    """
    Fonction permettant d'avancer au statut suivant pour le jeu, boucle sur l'indice maximal possible (retour à 0)
    """
    global statut_en_cours
    global statuts_jeu

    if statut_en_cours < len(statuts_jeu)-1:
        statut_en_cours += 1
    else:
        statut_en_cours = 0

def initialisation_partie():
    """
    Fonction permettant d'initialiser toutes les variables du jeu aux bonnes valeurs par défaut avant de commencer une partie
    """
    global score
    global min_score
    global bonus_score
    global raquette
    global scotch
    global balle
    global raquette_x_float
    global balle_x_float
    global balle_y_float
    global direction_balle
    global matrice_briques
    global briques_restantes
    global game_over
    global vitesse_balle
    global tableau_fini

    raquette.x = 140
    raquette.y = 160
    raquette_x_float = float(raquette.x) 

    balle.x = raquette.centerx - 2
    balle.y = raquette.y - 4 - 1
    balle_x_float = float(balle.x)
    balle_y_float = float(balle.y)
    vitesse_balle = 100.0
    direction_balle = [0.0, 0.0]

    matrice_briques = np.ones((6, 8), dtype=int)
    briques_restantes = np.sum(matrice_briques)

    scotch = True
    score = 0.0
    min_score = 100.0
    bonus_score = 900.0
    game_over = False
    tableau_fini = False


# Game loop
while en_cours:
    # -------------------------------------------
    # --- Update général --- évènements ponctuels
    # -------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # ----------------------
    # --- Update général ---
    # ----------------------
    input_joueur = pygame.key.get_pressed()

    if statuts_jeu[statut_en_cours] == "menu":
        # --------------
        # --- Update ---
        # --------------
        if input_joueur[pygame.K_RETURN]:
            # On lance l'initialisation si le joueur appuis sur entrée depuis le menu principal
            statut_suivant()

        # ------------
        # --- Draw ---
        # ------------
        # On vide l'écran pour le remplir d'une couleur unie RVB
        canvas.fill((30, 30, 50))
        # Affichage du texte du menu principal
        afficher_texte("SPEEDRUN LE CASSE BRIQUE", 62, 50)
        afficher_texte("Appuyez sur entree pour lancer une partie", 35, 75)

    elif statuts_jeu[statut_en_cours] == "init":
        # --------------
        # --- Update ---
        # --------------
        # On lance la fonction d'initialisation du jeu avant d'avancer au statut suivant (=lancer la partie)
        initialisation_partie()
        statut_suivant()

        # ------------
        # --- Draw ---
        # ------------
        # On vide l'écran pour le remplir d'une couleur unie RVB
        canvas.fill((30, 30, 50))

    elif statuts_jeu[statut_en_cours] == "jeu":
        # --------------
        # --- Update ---
        # --------------
        # Si aucune conditio nde gameover n'a été rencontrée
        if game_over == False:
            # Appuis sur la touche Q
            if input_joueur[pygame.K_q]:
                # Déplacement raquette à gauche
                raquette_x_float -= vitesse_raquette * delta

                # Collision mur gauche, on reste collé
                if raquette_x_float <= 10:
                    raquette_x_float = 10

                # Si la balle est collée, on la déplace avec la raquette sur la même vitesse
                if scotch == True:
                    balle_x_float -= vitesse_raquette * delta
                    if raquette_x_float == 10: # la raquette à touché le bord gauche, la balle doit rester au centre
                        balle_x_float = raquette_x_float + (raquette.width / 2) - 2

            # Appuis sur la touche D
            if input_joueur[pygame.K_d]:
                # Déplacement raquette à droite
                raquette_x_float += vitesse_raquette * delta

                # Collision mur droit, on reste collé
                if raquette_x_float >= 10 + 213 - raquette.width: 
                    raquette_x_float = 10 + 213 - raquette.width

                # Si la balle est collée, on la déplace avec la raquette sur la même vitesse
                if scotch == True:
                    balle_x_float += vitesse_raquette * delta
                    if raquette_x_float == 10 + 213 - raquette.width: # la raquette à touché le bord droit, la balle doit rester au centre
                        balle_x_float = raquette_x_float + (raquette.width / 2) - 2

            # Si la balle est scotchée, un appuis sur espace la lancera (par défaut en diagonale haut gauche (vecteur -1,-1))
            if scotch == True:
                if input_joueur[pygame.K_SPACE]: 
                    direction_balle = [-1.0, -1.0]
                    scotch = False
            else:
                # déplacement de la balle selon le vecteur direction et la vitesse
                balle_x_float += direction_balle[0] * vitesse_balle * delta
                balle_y_float += direction_balle[1] * vitesse_balle * delta

                # Collision avec la raquette
                if balle_y_float > raquette.y - balle.height:
                    if balle_x_float + balle.width >= raquette_x_float and balle_x_float <= raquette_x_float + raquette.width:
                        balle_y_float = raquette.y - balle.height
                        direction_balle[1] = - direction_balle[1]

                # Collision avec les murs
                if balle_x_float < 10: # Gauche
                    balle_x_float = 10
                    direction_balle[0] = - direction_balle[0]

                if balle_x_float > 10 + 213 - balle.width: # Droite
                    balle_x_float = 10 + 213  - balle.width
                    direction_balle[0] = - direction_balle[0]

                if balle_y_float > 10 + 160 - balle.height: # Bas = gameover
                    balle_y_float = 10 + 160 - balle.height
                    direction_balle[1] = - direction_balle[1]
                    vitesse_balle = 0.0
                    game_over = True

                if balle_y_float < 10: # Haut
                    balle_y_float = 10
                    direction_balle[1] = - direction_balle[1]

                # Retour aux valeurs en integer pour le positionnement précis de la balle en pixel et le check de collisions avec les briques
                balle.x = round(balle_x_float)
                balle.y = round(balle_y_float)

                # Collision avec les briques
                for i in range(0, 6):
                    for j in range(0, 8):
                        if matrice_briques[i, j] == 1:
                            # La brique est active
                            brique_reference.x = 21 + (j * 24)
                            brique_reference.y = 20 + (i * 9)

                            if balle.colliderect(brique_reference):
                                # Il y a collision entre la balle et la brique
                                matrice_briques[i, j] = 0                       # Brique détruite
                                score += min_score + bonus_score                # Mise à jour du score
                                briques_restantes = np.sum(matrice_briques)     # Mise à jour du nb de brique restantes
                                if briques_restantes == 0:
                                    # S'il n'y a plus de brique, la partie est terminée
                                    tableau_fini = True
                                    game_over = True

                                # Gestion du rebond sur les briques
                                intersection = balle.clip(brique_reference)
                                if intersection.width < intersection.height:
                                    # Collision sur l'horizontal
                                    direction_balle[0] = - direction_balle[0]
                                else:
                                    # Collision sur le vertical
                                    direction_balle[1] = - direction_balle[1]

                                # Sortie de la boucle pour éviter de détruire simultanément plusieurs briques durant la même frame
                                break

            # Retour aux valeur en integer pour le positionnement précis de la raquette et de la balle (si collée) en pixel
            raquette.x = round(raquette_x_float)
            if scotch:
                balle.x = round(balle_x_float)
                balle.y = raquette.y - 4 - 1

            # Diminution de la valeur actuelle de la brique (plus le temps passe, moins cela rapporte de points, mini=100)
            bonus_score -= round(10.0 * delta, 2)
            if bonus_score <= 0.0:
                bonus_score = 0.0

            # ------------
            # --- Draw ---
            # ------------
            # On vide l'écran pour le remplir d'une couleur unie RVB
            canvas.fill((30, 30, 50))
        
            # Contour noir de la zone de jeu
            pygame.draw.rect(canvas, (0, 0, 0), (0, 0, 10, 180))
            pygame.draw.rect(canvas, (0, 0, 0), (0, 0, 233, 10))
            pygame.draw.rect(canvas, (0, 0, 0), (223, 0, 10, 180))
            pygame.draw.rect(canvas, (0, 0, 0), (0, 170, 233, 10))

            # Affichage de la raquette du joueur
            pygame.draw.rect(canvas, (255, 255, 255), raquette)

            # Affichage des briques
            for i in range(0, 6):
                for j in range(0, 8):
                    if matrice_briques[i, j] == 1:
                        pygame.draw.rect(canvas, (0, 255, 255), (21 + (j * 24), 20 + (i * 9), brique_reference.width, brique_reference.height))

            # Affichage de la balle
            pygame.draw.rect(canvas, (255, 255, 255), balle)

            # UI (textes à droite, score etc.)
            afficher_texte("Briques", 234, 7)
            afficher_texte("restantes: " + str(briques_restantes), 234, 25)
            afficher_texte("Score:", 234, 45)
            afficher_texte(f"{score:.2f}", 234, 63)
            afficher_texte("Valeur d'une", 234, 100)
            afficher_texte("brique:", 234, 118)
            afficher_texte(f"{100 + bonus_score:.2f}", 234, 136)

        else: # Condition de gameover rencontrée, on avance au staut suivant : vers le gameover
            statut_suivant()

    else: # Seul statut restant : gameover
        # --------------
        # --- Update ---
        # --------------
        if input_joueur[pygame.K_SPACE]:
            # On revient au menu principal via un appuis sur la touche espace (on avance de statut)
            statut_suivant()
        
        # ------------
        # --- Draw ---
        # ------------
        # On vide l'écran pour le remplir d'une couleur unie RVB
        canvas.fill((30, 30, 50))
        # Affichage de fin de partie, score
        if tableau_fini == False:
            afficher_texte("GAME OVER", 120, 50)
        else:
            afficher_texte("JEU TERMINE", 120, 50)
        afficher_texte(f"Votre score: {score:.2f}", 100, 75)
        afficher_texte("Appuyez sur espace pour retourner au menu", 35, 120)
    

    # redimensionne et dessine de la surface (à l'échelle) sur la fenêtre + MAJ afficahge jeu
    canvas_redimensionne = pygame.transform.scale(canvas, (LARGEUR_FENETRE, HAUTEUR_FENETRE))
    fenetre.blit(canvas_redimensionne, (0, 0))
    pygame.display.flip()

    # Régler les images par seconde à 60
    delta = clock.tick(60) / 1000.0

# Fin du programme
pygame.quit()