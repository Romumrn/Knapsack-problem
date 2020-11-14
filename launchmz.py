import json
import os
from time import perf_counter 


with open('Test.json') as json_file: 
    data = json.load(json_file) 


## forme du fichier a generé
# n = 6;
# maximum = 9;
# prix = [1,15,10,7,8,10];
# poid = [1,4,3,2,5,6];

poidmax = 10000

for instance in data:
    print( instance)
    prix = []
    poid = []
    for objet in data[instance]:
        prix.append( str(data[instance][objet][0]*1000000)[0:4] )
        poid.append( str(data[instance][objet][1]*1000000)[0:4] ) 
    
    n = len(prix)
    fichier = open("valeur.dzn", "w")
    fichier.write("n = "+str(n)+";\n")
    fichier.write("maximum = "+str(poidmax)+";\n")
    fichier.write("prix = "+str(prix).replace("'", "")+";\n")
    fichier.write("poid = "+str(poid).replace("'", "")+";\n")
    fichier.close()

    cmd = "minizinc --solver gecode sac.mzn"
    # Start the stopwatch / counter 
    tps1 = perf_counter()

    os.system(cmd) 

    # Start the stopwatch / counter 
    tps2 = perf_counter()
    print(tps2 - tps1) 


