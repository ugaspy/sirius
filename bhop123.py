a,b,c,d,e=map(int,input('a b c d e:').split())
k=0
for x in range(1001):
   if a*x**3+b*x**2+(c+d)*x-e==0:
       print(x,end=' ')
       k+=1
print(k)
