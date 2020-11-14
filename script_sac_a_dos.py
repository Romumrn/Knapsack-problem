from algo import *
from generation_instance import *



'''
#génération des instances

instances_normal=generation_plusieurs_instances(nb_objet=30,nb_instance=10,info_taille="normal",info_duree="normal")
with open('instances_normal.json', 'w', encoding='utf-8') as f:
    json.dump(instances_normal, f, indent=4)


instances_TH_DL=generation_plusieurs_instances(nb_objet=30,nb_instance=10,info_taille="high",info_duree="light")
with open('instances_TH_DL.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TH_DL, f, indent=4)

instances_TH_DH=generation_plusieurs_instances(nb_objet=30,nb_instance=10,info_taille="high",info_duree="high")
with open('instances_TH_DH.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TH_DH, f, indent=4)

instances_TL_DL=generation_plusieurs_instances(nb_objet=30,nb_instance=10,info_taille="light",info_duree="light")
with open('instances_TL_DL.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TL_DL, f, indent=4)

instances_TL_DH=generation_plusieurs_instances(nb_objet=30,nb_instance=10,info_taille="light",info_duree="hight")
with open('instances_TL_DH.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TL_DH, f, indent=4)
'''

#Regardons d'abord pour les instances normales

with open('instances_normal.json') as json_data:
    dict_instances_normal= json.load(json_data)


resultat_brut_final=dict()
resultat_duree_final=dict()
resultat_taille_final=dict()
resultat_rapport_final=dict()

for key,value in dict_instances_normal.items():
    liste_instance=dict_instance_to_liste_instance(value)
    print("résultat pour l'",key)
    liste_resultat_brut=force_brut(liste_instance, 20)
    resultat_brut=(len(liste_resultat_brut[0]),liste_resultat_brut[1])
    print("résultat brut", len(liste_resultat_brut[0]),liste_resultat_brut[1])
    liste_resultat_duree =glouton(liste_instance, 20, duree)
    resultat_duree=(len(liste_resultat_duree[0]),liste_resultat_duree[1])
    print("résultat pour la duree",len(liste_resultat_duree[0]),liste_resultat_duree[1])
    liste_resultat_taille =glouton(liste_instance, 20, taille)
    resultat_taile=(len(liste_resultat_taille[0]),liste_resultat_taille[1])
    print("résultat pour la taille",len(liste_resultat_taille[0]),liste_resultat_taille[1])   
    liste_resultat_rapport =glouton(liste_instance, 20, rapport)
    resultat_rapport=(len(liste_resultat_rapport[0]),liste_resultat_rapport[1])
    print("résultat pour le rapport",len(liste_resultat_rapport[0]),liste_resultat_rapport[1])
    resultat_brut_final.append(resultat_brut)
    resultat_duree_final.append(resultat_duree)
    resultat_taille_final.append(resultat_taille)
    resultat_rapport_final.append(resultat_rapport)
