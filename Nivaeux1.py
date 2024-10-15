# NIVAEUX 1


#declaration des fonctions 
def table(A,b,c,d):
   for lab in range (A,b+1):
    if A<=b : 
     print("table de {}".format(lab))
     for i in range (c,d+1):
      print("{}*{}={}".format(lab,i,lab*i))
     A=A+1
#appel de fonction
table(1,2,6,50)
