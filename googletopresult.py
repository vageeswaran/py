import urllib2,re
s=raw_input('enter your query:')
s=re.sub('\s\s+','',s)
s=s.replace(' ','+')
if s[-1]=='+':
    s=s[:-1]
i=0
url="https://www.google.co.in/search?q="+s+"&num="+str(i+99)+"&start="+str(i)
headers = { 'User-Agent' : 'Mozilla/5.0' }

def get(url):
    try:
        req = urllib2.Request(url, None, headers)
        p=urllib2.urlopen(req).read()
        print url
        a=[]
        p=p.split('<h2 class="hd">')
        p=p[1]
        p=p.split('<h3 class="r">')
        p=p[1:]
        for s in p:
            u=s.split('<a href="')
            u=u[1].split('"')
            u=u[0]
            u=u.split('&amp;')
            u=u[0].split('=')
            u=u[1]
            z=s.split('<span class="st">')[1].split('</span>')[0]
            z=re.sub('<.*?>','',z)
            b=[]
            b.append(z)
            b.append(u)
            a.append(b)
    except Exception:
            print url
    return a

a=get(url)
