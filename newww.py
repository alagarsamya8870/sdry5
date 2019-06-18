from itertools import combinations
x,y=map(int,input().split())
g=len(str(x))
a=list(combinations(str(x),g-y))
a=(sorted(a))
l="".join(a[0])
print(l)
