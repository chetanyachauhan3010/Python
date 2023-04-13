x,y,z=10,20,30

'''
if x>y and x>z:
    print("X is greatre")
elif y>x and y>z:
    print("Y is greater")
else:
    print("Z is greater")
'''

output="X" if x>y and x>z else "Y" if y>x and y>z else "Z"
print(output," is greater")
    
