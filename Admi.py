
#DEFINIR LES NOMBRE D ' ADMIT EN L2


#entre la moyene des eleve
print("entrer la moyen de 10 élève :")
#enregistrer les variable
elevadmi = 0
elevnonadmi = 0
#commencer le boucle
for i in range(1,11):
   moyene = input("élève N°{} :".format (i))
#inserrer la condion pour choiisire les note le plus elever
if int(moyene)  <= 10:
        elevadmi = elevadmi+1
#afficher le resulta
print ("les nombre d'élève admit sont :" + str(elevadmi))
#FIN
      