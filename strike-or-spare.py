from math import gcd
for _ in range(int(input())):
    t = int(input())
    if t == 1:
        p = 1
        q = 1
    else:
        q = 9*10**(t-1)
        if t%2 == 0:
            p = 9*10**(t//2-1)
        else:
            p = 9*10**(t//2)
    d = gcd(p,q)
    p = p/d
    q = q/d
    print(int(p),int(q))
