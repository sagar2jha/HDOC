const = 10000000
from itertools import permutations as pnc
from functools import reduce
A,B = map(int,input().split())
a = str(A)
b = list(pnc(a))
m = lambda x,y : x+y
e = const
for i in b: 
    L = int(reduce(m, i))
    if L > B:
        if e > L:
            e = L
if e == const:
    print(-1)
else:
    print(e)
