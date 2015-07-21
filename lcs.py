s=raw_input('first string')
s1=raw_input('second string')
m=len(s)
n=len(s1)

def lcs1(x,y,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1+lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))

def lcs(x,y,m,n):
    l=[[0]*(n+1) for i in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    
    idx=l[m][n]
    
    z=['*']*idx
    
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            z[idx-1]=x[i-1]
            i-=1
            j-=1
            idx-=1
        elif l[i-1][j]> l[i][j-1]:
            i-=1
        else:
            j-=1
    print "lcs of "+x+' & '+y +' is '+''.join(z)+' of length '+str(l[m][n])
lcs(s,s1,m,n)
