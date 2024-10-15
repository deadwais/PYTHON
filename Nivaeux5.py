# faire une demande au utilisateur de saisir des valeur
n=int(input("entrer la valeur de n "))
p=int(input("entrer lavaleur de p "))
x=n-p;pr=n;i=1;nfact=0
# faire une foction qui peut calculer le factoriel d'un nombre
while i<n-1:pr=pr*(n-i);i=i+1
if pr>nfact:nfact=pr
pr=p;i=1;pfact=0
while i<p-1:pr=pr*(p-i);i=i+1
if pr>pfact:pfact=pr
pr=x;i=1;xfact=0
while i<x-1:pr=pr*(x-i);i=i+1
if pr>xfact:xfact=pr
# cree un fonction qui peut resoudre le probleme du C^n(p)
resultat= nfact/(pfact*xfact)
print(resultat)
    
