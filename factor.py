import sys

s=sys.stdin.readline().split('\n')[0]
s=s.split()
n=int(sys.stdin.readline().split('\n')[0])
a=[]
for i in xrange(1,n/2+1):
    if n%i==0:
        v=str(i)+','+str(n/i)
        a.append(v)
c=[]
for x in a:
    z=x.split(',')
    z=z[0]+z[1]
    z=list(set(list(z)))
    flag=0
    for i in z:
        if x.count(i)!=s.count(i):
            flag=1
            break

    if flag==0:
        c.append(x)
        break

c=c[0]
c=c.split(',')
x=c[0]
c=c[1]
if x<c:
    print x,c
else:
    print c,x

