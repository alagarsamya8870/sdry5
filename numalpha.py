a=input()
b=0
c=0
for i in a:
    if(i.isnumeric()):
        b+=1
    elif(i.isalpha()):
        c+=1
if(c>=1 and b>=1):
    print("Yes")
else:
    print("No")
