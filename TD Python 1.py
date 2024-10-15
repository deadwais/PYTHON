# demander la valeur au utilisateur
vola = int(input("ampdiro volanao manafio Ar"))
# enancer au programe les uniter monaitère
euro = 4217
dollars = 4000
# demmander au utilisateur les uniter qu'il veul avoir
chois_du_joureur = int(input("si vou vouler convertir en € veullier appuier sur 1 , si c'est en $ appuier sur 2 :"))
# afficher le resultat
if chois_du_joureur == 1:
    print( "vous avezs : " +str(vola/euro) + "€ " )
else :
    print( "vous avezs : "+ str(vola/dollars) +  "$ " )

# fin du programme 
