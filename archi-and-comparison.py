<<<<<<< HEAD
for _ in range(int(input())):
    a,b,n = map(int,input().strip().split())
    if n%2 == 0:
        if abs(a)>abs(b):
            print(1)
        elif abs(a)<abs(b):
            print(2)
        elif abs(a) == abs(b):
            print(0)
    else:
        if a>b:
            print(1)
        elif a<b:
            print(2)
        elif a==b:
            print(0)
=======
for _ in range(int(input())):
    a,b,n = map(int,input().strip().split())
    if n%2 == 0:
        if abs(a)>abs(b):
            print(1)
        elif abs(a)<abs(b):
            print(2)
        elif abs(a) == abs(b):
            print(0)
    else:
        if a>b:
            print(1)
        elif a<b:
            print(2)
        elif a==b:
            print(0)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
