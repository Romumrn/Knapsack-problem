% Probleme du sac a dos

include "valeur.dzn";


int: n; % nombre d'objet dans la liste d'objet
set of int: OBJ = 1..n; 
float: maximum; % Poid maximal du sac a dos 
array[OBJ] of int: prix; % Liste des prix
array[OBJ] of int: poid; % Liste des poids 

array[OBJ] of var int: x; % vecteur d'objet 

constraint forall(i in OBJ)(x[i] >= 0 ); %Chaque objet doit etre 0 ou 1, present dans le sac  ou absent)
constraint forall(i in OBJ)(x[i] < 2 ); %Chaque objet doit etre 0 ou 1, present dans le sac  ou absent)
constraint sum(i in OBJ)(poid[i] * x[i]) <= maximum; % la somme des poids est inferieur ou egal au maximun
solve maximize sum(i in OBJ)(prix[i] * x[i]); % La contrainte a maximiser est la somme des prix des objets dans le sac a dos

output ["Object = ", show(x), "\n","Price = ",show(sum(i in OBJ)(prix[i] * x[i])) ];