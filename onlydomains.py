f=open('govlinks.txt','r')
c=f.read()
c=c.split('\n')
f.close()
c=list(set(c))
url=[]
for s in c:
    s=s.replace('://','#')
    s=s.split('/')[0]
    s=s.replace('#','://')
    url.append(s)
c=url
c=list(set(c))
f=open('govlinks1.txt','a')
f.write('\n'.join(c))
f.close()

