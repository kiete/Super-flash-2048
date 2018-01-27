from A2048 import *
from Tkinter import *
#dictionnaire des couleurs que l'on donnera aux cases entourant les nombres
couleur = {2:"#FEEB6A",4:"#FEBE6A",8:"#FEA56A",16:"#FE836A",32:"#FE6A6A",64:"#FE6AAF",128:"#EFFE12",256:"#FEA812",512:"#FE6912",1024:"#FE3A12",2048:"#FE00DC"}
def act_canvas():
    #fonction servant a actualiser le canvas
    global couleur
    global fen
    #les boutons ne pouvant rien renvoyer j'ai choisi de rendre la liste globale pour faciliter la gestion
    global liste
    canvas = Canvas(fen,bg="white",height = 512 , width = 512)
    #a chaque actualisation du canevas on procedera a l'ajout d'une case de difficultee
    liste = add_dif(liste)
    #on cree les barres horizontales
    for i in range (3):
        palier = 128*(i+1)
        ligne = canvas.create_line(palier, 0, palier, 512, fill = "#F7E8B7")
        ligne = canvas.create_line(0, palier, 512, palier, fill = "#F7E8B7")
    #puis on cree les cases
    for i in range (4):
        for j in range (4):
            #on n'affichera pas les cases vallant 0
            if liste[j][i]!=0:
                #les rectangles sont derriere les nombres et la couleurs depends de ce dernier
                canvas.create_rectangle(i*128+10,j*128+10,(i+1)*128-10 , (j+1)*128-10 ,fill = couleur[liste[j][i]])
                #le +64 apres les cordonnes est la car les nombres doivent etre au centre de la case de 128px
                canvas.create_text(i*128+64 , j*128+64 , text = liste[j][i], fill = "white" , font = "arial 64")
    #on pense a afficher le canvas
    canvas.grid(row=1,column=1)
#les fonctions suivantes ont ete realises car les boutons ne peuvent rien renvoyer il fallais donc
#coder une fonction par action realisable je ne detaillerais le fonctionnement que de d_l() car les
#autres sont les memes
def d_l ():
    #on pense a appeller la liste
    global liste
    #on fait le deplacement
    liste = mouve(liste,"left")
    #on pense aussi a actualiser le canvas
    act_canvas()
def d_r():
    global liste
    liste = mouve(liste,"right")
    act_canvas()
def d_b():
    global liste
    liste=mouve(liste,"bottom")
    act_canvas()
def d_t():
    global liste
    liste = mouve(liste,"top")
    act_canvas()
def start():
    #se lance en premier et permmet la creation de la fenetre
    global liste
    global fen
    #on cree une liste vierge
    liste=gen_vierge()
    #on commence avec 3 cases colores
    for i in range (3):
        liste = add_dif(liste)
    fen = Tk()
    #on cree les boutons
    b_g=Button(fen,text = "<",command = d_l).grid(row=1,column=0,sticky = "nesw")
    b_g=Button(fen,text = ">",command = d_r).grid(row=1,column=2,sticky = "nesw")
    b_g=Button(fen,text = "top",command = d_t).grid(row=0,column=1,sticky = "nesw")
    b_g=Button(fen,text = "bottom",command = d_b).grid(row=2,column=1,sticky = "nesw")
    #puis le canvas au centre
    canvas = Canvas(fen,bg="black",height = 512 , width = 512)
    #on cree les barres horizontales
    act_canvas()
    fen.mainloop()
start()
