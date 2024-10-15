# demander les deux nombre au utilisateur 
nbr1 = int(input("entrer le premier nombre"))
nbr2 = int(input("entrer le deuxième nombre"))
if nbr1>0 and nbr2>0 :
    print("le produit de ces deux valeur serait positif")
elif  nbr1==0 or nbr2==0 :
    print("le produit de ces deux valeur serait nul")
else :
    print("le produit de ces deux valeur serait negatif")