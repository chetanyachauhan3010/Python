x,y=10,20
'''
if x>y:print("X is greater....")
else:print("Y is greater...")
'''

'''
if x>y:
print("X is greater....")      #indentation error
else:
    print("Y is greater...")

'''

'''
if x>y:
    print("X is greater....")         #NO ERROR
else:
    print("Y is greater...")
'''

print("X" if x>y else "Y")

#OR

optput="X" if x>y else "Y"
print(output," is greater...")
