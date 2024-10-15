# reccolter la valeur d'une porte money
money_actuel = int(input("entree le montomt de votre argent"))
# cree une produit d' une valeur qui est egale a 50
produit = int(input ("entree le prix du produit que vous vouler acheter"))
# afficher la nouvel valeur du porte money
nouvel_montant = (money_actuel - produit)
print("ny volanao sisa dia " +  str(nouvel_montant)  + "AR")
# place de cinema
# l' age de la personne 
age_de_la_personne = int(input("entree votre age"))
# si la persone et mineur alors elle doit payer 5€ ,si nom elle devrat payer 12€
if age_de_la_personne < 18 :
    print("vous devrer payer 5€")
else: 
    print("vous dever payer 12€")
# demander si di elle veu du popcorne 
print("vous volez du popcorne?")
print("si oui vous devez payer 17€")
      


