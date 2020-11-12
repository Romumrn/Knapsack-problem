videos = [('Video1', 114, 4.57), ('Video2', 32, 0.630),('Video3', 20, 1.65), ('Video4', 4, 0.085),('Video5', 18, 2.15), ('Video6', 80, 2.71),('Video7', 5, 0.320)]

import json


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


with open('Test.json') as json_data:
    dict_instances= json.load(json_data)


for key,value in dict_instances.items():
    liste_instance=dict_instance_to_liste_instance(value)
    liste_resultat =glouton(liste_instance, 5, duree)
    print(len(liste_resultat[0]),liste_resultat[1])
