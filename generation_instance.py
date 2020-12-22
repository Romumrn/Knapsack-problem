from random import random
import json
import numpy as np

def uniforme(a,b):
    return a+(b-a)*random()


def generation_une_instance(nombre_objet,info_taille,info_duree):
    iteration=[i+1 for i in range(nombre_objet)]
    dict_object=dict()
    for i in iteration:
        video=list()
        if info_taille=="high":
            mu = 4.0
            sigma = 0.5
            taille=np.random.randn(1) * sigma + mu
            taille=taille[0]
        elif info_taille=="light":
            mu= 1.0
            sigma=0.5
            taille=np.random.randn(1) * sigma + mu
            taille=taille[0]
        else:
            taille=uniforme(0,5)
            
        if info_duree=="high":
            mu = 80.0
            sigma = 10.0
            duree=np.random.randn(1) * sigma + mu      
            duree=duree[0]      
        elif info_duree=="light":
            mu= 30.0
            sigma=10.0
            duree=np.random.randn(1) * sigma + mu
            duree=duree[0]
        else:
            duree=uniforme(0,100)
        num_object="objet "+str(i)
        dict_object[num_object]=[duree, taille]
    return dict_object


def generation_plusieurs_instances(nb_objet,nb_instance,info_taille,info_duree):
    iteration=[i+1 for i in range(nb_instance)]
    dict_instance=dict()
    for i in iteration:
        instance_seul=generation_une_instance(nb_objet,info_taille,info_duree)
        num_instance="instance"+str(i)
        dict_instance[num_instance]=instance_seul
    return dict_instance

generation_plusieurs_instances(nb_objet=1000,nb_instance=100,info_taille="high",info_duree="light")
generation_plusieurs_instances(nb_objet=1000,nb_instance=100,info_taille="high",info_duree="light")
generation_plusieurs_instances(nb_objet=1000,nb_instance=100,info_taille="high",info_duree="high")
generation_plusieurs_instances(nb_objet=1000,nb_instance=100,info_taille="light",info_duree="light")
generation_plusieurs_instances(nb_objet=1000,nb_instance=100,info_taille="light",info_duree="hight")


