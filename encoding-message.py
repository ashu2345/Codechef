<<<<<<< HEAD
charlist = list(map(chr,range(97,123)))
for _ in range(int(input())):
    n = int(input())
    string = list(input())
    for i in range(0,n-1,2):
        string[i],string[i+1] = string[i+1],string[i]
    for i in range(n):
        string[i] = charlist[25-charlist.index(string[i])]
    print(''.join(string))
=======
charlist = list(map(chr,range(97,123)))
for _ in range(int(input())):
    n = int(input())
    string = list(input())
    for i in range(0,n-1,2):
        string[i],string[i+1] = string[i+1],string[i]
    for i in range(n):
        string[i] = charlist[25-charlist.index(string[i])]
    print(''.join(string))
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
