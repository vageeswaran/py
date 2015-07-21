import time as t
def power1(x,y):
    return pow(x,y)
def power(x,y):
    if y==0:
        return 1
    z=power(x,y/2)
    if y%2==0:
        return z*z
    else:
        return x*z*z

x,y=map(int,raw_input().split())
st=t.time()
print power(x,y)
print t.time()-st

st=t.time()
print power1(x,y)
print t.time()-st
