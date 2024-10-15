
import sys
sys.setrecursionlimit(2000)
def zero(n):
    """fonction qui donne la valeur de la factoriel d'un nombre entiers.
    
    Cette fonctions fait presque la moitieller de ce projet pour compte le nombre du zéro depuis l'arrière.
    
    Parameters 
    ----------
    n : int 
      le nombre entier.
      celle que l'utilisateur a entrer pour s'avoir sa nombre de zéro en fesant sa factoriel.
      
    Return 
    ------
    int 
       Le produit factoriel de l'entier n qui est égal à n*(n-1)factoriel.
    """
#après avoir obtenue le resultat de la factoriel l'entier du variable result_brutte 
#nous allons passer au boucle qui vas nous aider pour compter le nombre de zero depuis l'arri
    
    def factoriel(n):
            if n==0:
                return (1)
            else :return (n*factoriel(n-1))
    p=factoriel(n)
    g=str(p)
    r=list(reversed(g))
    u=0
    for i in r:
          if i=='0':
                u+=1
          else:break
    print(u)
    print(factoriel(n))
    
zero(1900)
  