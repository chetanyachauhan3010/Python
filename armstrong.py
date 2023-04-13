x=407
arm=0
b=x
c = len(str(x))

while x!=0:
    a=x%10
    arm=arm+a**c
    x=x//10

if(b==arm):
    print("The Number is Armstrong.")
else:
    print("The Number is not Armstrong.")
    


