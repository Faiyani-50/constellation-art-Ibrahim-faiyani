import turtle

# 1. Configuration de la fenêtre
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1a1a2e")  # Fond bleu nuit
screen.title("Projet Constellation : L'Animal aux Vraies Étoiles")

t = turtle.Turtle()
t.speed(0)          # Vitesse maximale pour que le dessin soit instantané
t.pensize(2)
t.color("#48dbfb")  # Couleur des lignes de connexion (bleu néon)

# --- FONCTION POUR DESSINER UNE VRAIE ÉTOILE ---
def dessiner_etoile(taille, couleur):
    """Cette fonction dessine une étoile à 5 branches remplie de couleur"""
    t.setheading(0) # Réinitialise l'orientation de la tortue
    t.color(couleur)
    t.begin_fill()
    for _ in range(5):
        t.forward(taille)
        t.right(144)  # L'angle magique pour une étoile à 5 branches
    t.end_fill()
    t.color("#48dbfb") # On remet la couleur bleue pour la ligne suivante

# 2. LISTE DE TUPLES : Les coordonnées de la constellation (4 pattes)
pattes_avant = [(-30, 20), (-45, -50), (-30, 20), (-20, -50)] 
corps = [(-30, 20), (50, 10)]                                 
pattes_arriere = [(50, 10), (45, -60), (50, 10), (65, -50)]   
dos_et_queue = [(50, 10), (90, 40), (40, 40), (-30, 20)]      

etoiles = pattes_avant + corps + pattes_arriere + dos_et_queue

# 3. Tracé automatique du corps avec de VRAIES étoiles jaunes
t.penup()
if etoiles:
    t.goto(etoiles[0][0], etoiles[0][1])
    t.pendown()

for position in etoiles:
    x = position[0]
    y = position[1]
    t.goto(x, y)
    
    # On mémorise la position actuelle pour y dessiner l'étoile au centre
    pos_actuelle = t.position()
    t.penup()
    # On décale légèrement la tortue pour que l'étoile soit centrée sur la ligne
    t.goto(pos_actuelle[0] - 7, pos_actuelle[1] + 3) 
    t.pendown()
    
    dessiner_etoile(15, "#fff200") # Dessine une étoile jaune de taille 15
    
    t.penup()
    t.goto(pos_actuelle) # On revient à la ligne de la constellation
    t.pendown()

# 4. Dessin de la tête ronde (Remplie pour un rendu propre)
t.penup()
t.goto(-30, 20)  
t.pendown()

t.fillcolor("#1a1a2e") 
t.begin_fill()
t.circle(25)           
t.end_fill()
t.circle(25)           

# Vraies étoiles sur la tête ronde
t.penup()
t.goto(-30 - 7, 70 + 3)  # Haut du crâne
dessiner_etoile(15, "#fff200")

t.penup()
t.goto(-55 - 7, 45 + 3)  # Bout du museau
dessiner_etoile(15, "#fff200")

# 5. Ajout de petites oreilles pointues sur la tête ronde
t.penup()
t.goto(-20, 65)
t.pendown()
t.goto(-22, 85) # Oreille 1
t.goto(-27, 70)
t.goto(-32, 85) # Oreille 2
t.goto(-37, 65)

# 6. Un œil blanc brillant pour finaliser l'animal céleste
t.penup()
t.goto(-38, 48)
t.dot(6, "white")

# Cacher la tortue
t.hideturtle()

# Laisser la fenêtre ouverte
turtle.done()
