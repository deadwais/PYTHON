# exercice2
N = int(input("Saisir N :"))
oui = 0
nom = 0
for i in range(1,N+1):
    vote = input("avis{} :".format(i))
if vote=="oui":
    oui = oui+1
elif  vote =="nom":
    nom = nom+1
else :
    print(" ")
if oui<nom:
    print("nom")
elif oui==nom :
    print("egaliter")
else :
    print("oui")
#FIN