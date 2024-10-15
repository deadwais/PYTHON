from ast import Return


n=int(input("entrer un nbr : "))
x=n%2
y=n%3
z=n%5
w=n%7
if  x!=0 and y!=0 and z!=0 and w!=0 and n!=1 or n==2 or n==5 or n==3 or n==7 :
    resultat="vrais"
    Return(resultat)
elif x==0 or y==0 or z==0 or w==0 or n==1:
    resultat="faux"
    Return(resultat)
print(resultat)
