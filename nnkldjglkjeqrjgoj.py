n=153
m=list(str(n))
p=0
for i in range (len(str(n))):
    p+= (int(m[i])**len(str(n)))
print(p)²