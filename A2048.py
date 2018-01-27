from random import *
def print_tab (liste):
    #fonction permettant d'afficher le tableau de maniere plus lisible !
    for i in range (4) :
        print(liste[i])
    print ("\n")
    return False
def gen_vierge():
    #en effet le tableau est une liste de listes
    liste_vierge = []
    for i in range (4):
        liste_vierge.append([])
        for j in range (4):
            liste_vierge[i].append(0)
    return liste_vierge
def add_dif(liste):
    #ajoute un 2 ou un 4 a un emplacement libre du tableau
    #on dresse une liste d'emplacements libres
    libres = []
    #la ligne suivante nous permmet de generer un 2 ou un 4 de maniere aleatoire
    n = randint(1,2)*2
    for i in range(4):
        for j in range (4):
            if liste[i][j]==0:
                libres.append([i,j])
    if len(libres)==0:
        return False
    #si la liste est vide, il n'y a alors pas d'emplacements libres et la personne a perdue
    #on melange cette liste et on rajoute un 2 ou un 4 a la paire de coordonnes tiree
    shuffle(libres)
    x = libres[0][0]
    y = libres[0][1]
    liste[x][y]=n
    return liste
def mouve(liste,direction):
    #grosse fonction permettant de gerer les actions a realiser lors de chaque deplacement
    if (direction == "right") or (direction=="left"):
        if direction == "right":
            liste =meg_cumul(liste)
        elif direction == "left":
            liste = meg_cumul(liste)
            print_tab(liste)
            liste = meg_inv_liste(liste)
    else:
        if direction == "bottom":
            print ("bottom")
            liste=tourne(liste)
            liste =meg_cumul(liste)
            liste=tourne(liste)
        elif direction == "top":
            print("top")
            liste=tourne(liste)
            liste = meg_cumul (liste)
            liste = meg_inv_liste(liste)
            liste = tourne(liste)
    print_tab(liste)
    return liste
        
    return liste
def cumul (liste):
    #cette fonction prends une liste et cumule tous les nombres simmilaires en envoyant 
    #tout vers la droite, comme dans le jeu 2048
    #nous allons proceder de gauche a droite
    for j in range (3):
        for i in range (3):
            if liste[i] == liste[i+1]:
                liste[i+1]*=2
                liste[i]=0
            elif liste[i+1]==0:
                liste [i],liste[i+1] = liste[i+1],liste[i]
    return liste
def meg_cumul(liste):
    #permer d'etendre la fonction de cumul a une liste de listes
    new=[]
    for i in liste:
        new.append(cumul(i))
    return new
def inv_liste(liste):
    #cette fonction se rends utile pour caler les nombres a gauche apres un cumul 
    #qui les aura mis a droite
    new_liste = []
    for i in range(len(liste)):
        if liste[i]!=0:
            new_liste.append(liste[i])
    for i in range (4-len(new_liste)):
        new_liste.append(0)
    return new_liste
def meg_inv_liste(liste):
    #permet d'etendre l'inv_liste a une liste de listes
    new = []
    for i in liste:
        new.append(inv_liste(i))
    return new
def tourne (tab):
    #passe le vertical en horizontal ou vice-versa
    #permmet d'utiliser les fonctions de cumul de lignes aux colonnes
    #en effet en gros on peut proceder par tourne(cumul(tourne(liste)))
    nouveau = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            a=tab[i][j]
            nouveau[j].append(a)
    return nouveau


def main ():
    #fonction inactive qui peut servir a realiser des tests
    l=gen_vierge()
    for i in range (10):
        l = add_dif(l)
    print_tab (l)
    l=tourne(l)
    print_tab (l)
    l=meg_cumul(l)
    l=tourne(l)
    print_tab(l)
#    print_tab(l)
