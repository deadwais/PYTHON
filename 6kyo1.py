s=[1,2,3,4,5]
l=[]
while len(s)>1:
      l.append(s[0])
      l.append(s[-1]) 
      s.remove(s[0])
      s.pop() 
      s=s[::-1]
l.append(s[0])
s.pop()
print(l)