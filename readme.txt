README

Projet de l'UE "Graphe, Complexité, Combinatoire", réalisé par Théophile Tesseraud et Romuald Marin

Projet: problème du sac à dos.

Ce dépot se compose d'algorithmes et d'instances:

1) Les algorithmes:


- Le script generation_instance.py contient tous les algorithmes qui permet de générer différents types d'instances
- Le script algo.py contient tous les algorithmes pour faire tourner un algorithme gloutons et force brut.
- Le script lauchmz.py permet de faire tourner le solveur de contrainte sur un seul type d'instance.
- Le scirpt Sac.mzn contient l'algorithme utilisé par minizinc et lancé par launchmz.py
- Le script script_sac_a_dos permet de générer un seul type d'instance sous la forme json et de faire tourner les algorithme glouton et/ou force brut sur ce  type d'instance.
- Le script script_sac_a_dos_auto permet de générer plusieurs types d'instance sous la forme json et de faire tourner les algorithme glouton et/ou force brut et/ou avec le solveur de contrainte minizinc sur ces différents types d'instances.

Les résultats sont affichés directement dans la console ainsi que dans un fichier resultat.tsv
