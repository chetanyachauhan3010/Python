'''
x=0
def counter():
    global x
    while True:
        x += 1
        return x
 
counter()

counter()
'''

def counter():
    x=0
    while True:
        x +=1
        yield x

count= counter()
next(count)