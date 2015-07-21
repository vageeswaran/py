import re
pos=[]
dstr={}
final=[]
x="ababcdabcdcde"

for k in re.finditer(r"(?=(.+?)\1+)",x):
    #Find start of all overlapping strings
    pos.append(k.start())
i=0
for k in pos: #Find end of overlapping strings
    s=re.findall(r"^((.*)\2+)",x[k:])
    #print s
    dstr[i]=(k,len(s[0][0]))
    i=i+1
#print dstr.values()
k=0
while k< len(dstr.values())-1:           #remove smaller length overlapping result
    if dstr.values()[k+1][0]<dstr.values()[k][1]<dstr.values()[k+1][1]:
        pass
    else:
        final.append(dstr.values()[k][0])
    k=k+1
if dstr.values()[k-1][0] in final:
    pass
else:
    final.append(dstr.values()[k][0])
#print final
for k in final:             #remove strings
    s=re.sub(r"(.*)\1+",r"\1",x[k:])
    x=x[:k]+s
print x
