from operator import index


def mygcd(x):
  b=0
  s=0
  m=0
  j= x.split(",")
  for i in range(len(j)):
    k=j[i].split(" ")
    p=float(k[-2])
    o=float(k[-3])
    if k[-1]=='B'and (k[-2])==( k[-2].pi, ):
       b+=p*o
    elif k[-1]=='S':
       s+=p*o
    else:m+=1
  if m>0:
      print("Buy: {} Sell: {} Badly {}")
  else:
        print("Buy: {} Sell: {}".format(int(b),int(s)))
  
mygcd("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B")
mygcd(" MYSPACE 24.0 210 B, CITI 50 450 B")