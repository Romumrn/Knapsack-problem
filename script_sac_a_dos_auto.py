from algo import *
from generation_instance import *
from time import perf_counter 
import sys
'''

#génération des instances

instances_normal=generation_plusieurs_instances(nb_objet=25,nb_instance=5,info_taille="normal",info_duree="normal")
with open('instances_normal.json', 'w', encoding='utf-8') as f:
    json.dump(instances_normal, f, indent=4)

instances_TH_DL=generation_plusieurs_instances(nb_objet=25,nb_instance=5,info_taille="high",info_duree="light")
with open('instances_TH_DL.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TH_DL, f, indent=4)

instances_TH_DH=generation_plusieurs_instances(nb_objet=25,nb_instance=5,info_taille="high",info_duree="high")
with open('instances_TH_DH.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TH_DH, f, indent=4)

instances_TL_DL=generation_plusieurs_instances(nb_objet=25,nb_instance=5,info_taille="light",info_duree="light")
with open('instances_TL_DL.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TL_DL, f, indent=4)

instances_TL_DH=generation_plusieurs_instances(nb_objet=25,nb_instance=5,info_taille="light",info_duree="hight")
with open('instances_TL_DH.json', 'w', encoding='utf-8') as f:
    json.dump(instances_TL_DH, f, indent=4)

'''

res = open("resultat.tsv", 'a')

#Regardons d'abord pour les instances normales

instance = sys.argv[1]

with open(instance) as json_data:
    dict_instances_normal= json.load(json_data)

for key,value in dict_instances_normal.items():
    liste_instance=dict_instance_to_liste_instance(value)
    print("résultat pour l'",key)

    # print( "Methode brut")
    # tps1 = perf_counter()
    # liste_resultat_brut=force_brut(liste_instance, 20)
    # tps2 = perf_counter()
    # print("temps  d'execution : " , tps2 - tps1) 
    # print("résultat brut", len(liste_resultat_brut[0]),liste_resultat_brut[1])
    # res.write(instance + "\tbrut\t"+str(tps2 - tps1)+"\t"+str(len(liste_resultat_duree[0]))+'\t'+str(liste_resultat_duree[1])+'\n' )

    print( "Methode glouton durée")
    tps1 = perf_counter()
    liste_resultat_duree =glouton(liste_instance, 20, duree)
    tps2 = perf_counter()
    print("temps  d'execution : " , tps2 - tps1) 
    print("résultat pour la duree",len(liste_resultat_duree[0]),liste_resultat_duree[1])
    res.write(instance + "\tglouton durée\t"+str(tps2 - tps1)+"\t"+str(len(liste_resultat_duree[0]))+'\t'+str(liste_resultat_duree[1])+'\n' )

    print( "Methode glouton taille")
    tps1 = perf_counter()
    liste_resultat_taille =glouton(liste_instance, 20, taille)
    tps2 = perf_counter()
    print("temps  d'execution : " , tps2 - tps1) 
    print("résultat pour la taille",len(liste_resultat_taille[0]),liste_resultat_taille[1]) 
    res.write(instance + "\tglouton taille\t"+str(tps2 - tps1)+"\t"+str(len(liste_resultat_duree[0]))+'\t'+str(liste_resultat_duree[1])+'\n' )

    print( "Methode glouton rapport")
    tps1 = perf_counter()
    liste_resultat_rapport =glouton(liste_instance, 20, rapport)
    tps2 = perf_counter()
    print("temps  d'execution : " , tps2 - tps1) 
    print("résultat pour le rapport",len(liste_resultat_rapport[0]),liste_resultat_rapport[1])
    res.write(instance + "\tglouton rapport\t"+str(tps2 - tps1)+"\t"+str(len(liste_resultat_duree[0]))+'\t'+str(liste_resultat_duree[1])+'\n' )

