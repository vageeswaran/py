from urllib2 import urlopen as up
pg=up('http://cyberjournalist.org.in/links3.html').read()
pg=pg.split('href="')[1:]
url=[]
for s in pg:
    s=s.split('"')[0]
    if 'http' in s:
        url.append(s)

url=list(set(url))
f=open('govlinks.txt','a')
f.write('\n')
f.write('\n'.join(url))
f.close()
