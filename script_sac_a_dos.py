from algo import *



'''
instances=generation_instances(100,10)


with open('Test.json', 'w', encoding='utf-8') as f:
    json.dump(instances, f, indent=4)
'''




videos = [('Video1', 114, 4.57), ('Video2', 32, 0.630),('Video3', 20, 1.65), ('Video4', 4, 0.085),('Video5', 18, 2.15), ('Video6', 80, 2.71),('Video7', 5, 0.320)]



choix = force_brut(videos, 5)
duree_totale = choix[1]
choix_fichiers = [fichier[0] for fichier in choix[0]]
print(choix_fichiers, duree_totale)

'''
with open('Test.json') as json_data:
    dict_instances= json.load(json_data)


for key,value in dict_instances.items():
    liste_instance=dict_instance_to_liste_instance(value)
    liste_resultat =glouton(liste_instance, 5, duree)
    print(len(liste_resultat[0]),liste_resultat[1])
'''
