n=input()
a=[[0]*n for i in xrange(n)]
i=0
j=n/2
k=1
while k<=n*n:
    a[i][j]=k
    i-=1
    j+=1
    if k%n==0:
        i+=2
        j-=1
    else:
        if i<0:
            i+=n
        elif j==n:
            j=0
    k+=1
for i in xrange(n):
    s1=0
    s2=0
    for j in xrange(n):
        s1+=a[i][j]
        s2+=a[j][i]
        print a[i][j],
    print s1,s2
    print '\n'
        
