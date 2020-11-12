from random import random
import json

def uniforme(a,b):
    return a+(b-a)*random()


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

instances=generation_instances(100,10)


with open('Test.json', 'w', encoding='utf-8') as f:
    json.dump(instances, f, indent=4)
