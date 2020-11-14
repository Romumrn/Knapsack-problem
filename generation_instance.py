from random import random
import json
import numpy as np

def uniforme(a,b):
    return a+(b-a)*random()


def generation_une_instance_difficile(taille):
    iteration=[i+1 for i in range(taille)]
    dict_object=dict()
    mu = 4.0
    sigma = 1.0
    for i in iteration:
        video=list()
        duree=uniforme(0,100)
        taille=np.random.randn(1) * sigma + mu
        taille=taille[0]
        num_object="objet "+str(i)
        dict_object[num_object]=[duree, taille]
    return dict_object



def generation_une_instance(taille):
    iteration=[i+1 for i in range(taille)]
    dict_object=dict()
    for i in iteration:
        video=list()
        duree=uniforme(0,100)
        taille=uniforme(0,5)
        num_object="objet "+str(i)
        dict_object[num_object]=[duree, taille]
    return dict_object





def generation_instances(taille,nb_instance):
    iteration=[i+1 for i in range(nb_instance)]
    dict_instance=dict()
    for i in iteration:
        instance_seul=generation_une_instance(taille)
        num_instance="instance"+str(i)
        dict_instance[num_instance]=instance_seul
    return dict_instance
