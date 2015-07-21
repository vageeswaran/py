def shift(key, array):
    return array[-key:]+array[:-key]
global flag
for _ in xrange(input()):
    flag=0
    n=input()
    a=map(int,raw_input().split())
    if sum(a)>n or sum(a)==0:
        print -1
    else:
        for i in a:
            if i>(n-1):
                flag=1
                break
        if flag==1:
            print -1
        else:
            a=shift(2,a)
            print ' '.join(a)
