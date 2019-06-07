first,second=list(map(str,input().split()))
a=len(set(first))
b=len(set(second))
if a==b :
    print("yes")
else:
    print("no")
