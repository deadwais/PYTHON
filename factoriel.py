import sys
sys.setrecursionlimit(15000)
def zeros(n):
    def factoriel(n):
            if n == 0:
                return(1)
            else: return(n*factoriel(n-1))
    r = list(reversed(str(factoriel(n))))
    u = 0
    for i in r:
        if i == '0':
                u += 1
        else: 
            break
    return(u)






 
  