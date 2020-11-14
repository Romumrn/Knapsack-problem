videos = [('Video1', 114, 4.57), ('Video2', 32, 0.630),('Video3', 20, 1.65), ('Video4', 4, 0.085),('Video5', 18, 2.15), ('Video6', 80, 2.71),('Video7', 5, 0.320)]

import json



#Les différents composants de l'algorithùe glouton

def dict_instance_to_liste_instance(dict_instance):
    liste_instance=list()
    for key,value in dict_instance.items():
        temp_list=[key,value[0],value[1]]
        liste_instance.append(temp_list)
    return liste_instance

def duree(fichier):
    return fichier[1]
    
def taille(fichier):
    return 1 / fichier[2]
    
def rapport(fichier):
    return fichier[1] / fichier[2]

def glouton(liste, taille_max, choix):
    '''
    Algorithme qui résoult le problème du sac à dos selon une approche gloutonne dépéendant de 3 choix:
    
    - duree= approche basé sur la valeur de nos objet (on prend les objets de plus forte valeurs)
    - taille= approche basé sur la taille de nos objet (on prend les objets de plus petite taille en premier) 
    - rapport= approche basé sur le rapport duree/taille de nos objets
    '''
    triee =sorted(liste, key=choix, reverse=True)
    reponse = []
    totale_duree = 0
    taille = 0
    i = 0
    while i <len(liste) and taille <= taille_max:
        nom, d, t = triee[i] #nom, durée et taille
        if taille + t <= taille_max:
            reponse.append(nom)
            taille += t
            totale_duree += d
        i += 1
    return reponse, totale_duree


#Les différents composants de l'algo force brut

def int_to_bin(n, nb):
    ch =""
    while n > 0:
        r = n % 2
        n = n // 2
        ch =str(r) + ch
    ch = (nb -len(ch)) *"0"+ ch
    return ch

def ens_des_parties(ensemble):
    """ensemble est une liste de p-uplets"""
    nb =len(ensemble) #nombred'éléments
    n = 2 ** nb #nombre de parties
    parties = [] #l'ensemble des parties
    for i in range(1, n):
        ch = int_to_bin(i, nb)
        partie = []
        for j in range(len(ch)):
            if ch[j] =="1":
                partie.append(ensemble[j])
        parties.append(partie) #la partie construite est ajoutée à la liste
    return parties
    
def duree_totale(liste):
    d = 0
    for triplet in liste:
        d += triplet[1]
    return d
    
def taille_totale(liste):
    t = 0
    for triplet in liste:
        t += triplet[2]
    return t
    
def recherche(ens_parties, contrainte):
    duree_max = 0
    solution = []
    for partie in ens_parties:#un choix possible de fichiers
        duree = duree_totale(partie)
        taille = taille_totale(partie)
        if taille <= contrainte and duree > duree_max:
            duree_max = duree
            solution = partie
    return solution, duree_max


def force_brut(fichiers, taille_max):
    parties = ens_des_parties(fichiers)
    return recherche(parties, taille_max)

