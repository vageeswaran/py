from itertools import permutations as prm
import sys
s=list(sys.stdin.readline().split('\n')[0])
a=map(int,(sys.stdin.readline().split('\n')[0]).split())
i=1
b=[]
global flag
while i<=len(s):
    z=prm(s,i)
    b+=z
    i+=1
c=[]
for x in b:
    x=''.join(x)
    x=int(x)
    flag=0
    for z in a:
        if (x%z)==0:
            flag=0
        else:
            flag=1
            break

    if flag==0:
        c.append(x)
print max(c)
