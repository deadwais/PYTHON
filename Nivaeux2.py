# faire une demande au utilisateur d'entrer une sommpe en ariary
S=int(input("entrer votre somme en ariary svp :"))
# entrer les variable
f=S*5;d=S/4484;e=S/3985
# declaration des foctions 
def A (uniter,symbole):
    print("{}Ar -> {} {}".format(S,uniter,symbole))
# appel des fonction
A(f,"fmg");A(d,"$");A(e,"€")
