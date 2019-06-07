x,y=input().split()
z=len(x)
a=0
for i in range(0,z,1):
  if x[i]!=y[i]:
    a=a+1
if a==1:
  print("yes")
else:
  print("no")
