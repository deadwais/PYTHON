
# DETERMINER LES MOYEZNNE LES PLUS ELEVER PARMIS LES 10 MOYENNE ENTRER


#denancer les variable
max = 0
moyen =0
#faire ennter la moyenne des dix élèves
print("veuiller saisir la moyenne des dix élèves s'il vous plait :  ")
#comancer la boucle
for i in range (1,11) :
 moyene = int(input("élève N°{} :".format(i)))
#inserer la condition pour definrir la note plus élever
 if max <= moyene  :
     max = moyene
# afficher la moyenne la plus élever
print("la moyene la plus élever est :"+str(max))
#FIN