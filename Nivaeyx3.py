# faire une demande au utilisateur d'entrer une valeur en cm
s="oui"
while s =="oui":
  v=int(input("Entre une valeur en cm :"))
# entrer les variable
  mm=v*10;i=v/2.54;px=i/96;pt=i/72;pc=12*pt
# declaration des foctions 
  def A (uniter,symbole): print("{}cm -> {} {}".format(v,uniter,symbole))
# appel des fonction
  A(mm,"mm");A(i,"in");A(px,"px");A(pt,"pt");A(pc,"pc");s=(input("vouler vous entrer une autre valelur ?(veuiller repondre par oui ou nom) : " ))
if s=="nom":
 print("nous vous remercions de votre cooperation ")
#fin