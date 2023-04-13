a=21
b=19
#c=a+b
#d=a/b
#e=a-b
#f=a*b
#print(c)

#print("sum is ",c)
#print("sum of ",a," and ",b," is ",c)
#print("Sum of {} and {} is {}".format(a,b,c))
#print("Sum of {} and {} is {:.2f}".format(a,b,d))
#f-string
#print(f"Sum of {a} and {b} is {c}")
#Multi line print
#print(f"""
#1.Sum is {c}
#2.Div is (d}
#3.Sub is {e}
#4.MUl is {f}
#""")

#Walrus Operator (:=)
print("Sum is ",c:=a+b)

print(f"""
1.Sum is {(c:=a+b)}
2.Sub is {(b:=a-b)}
3.Div is {(d:=a/b):.2f}
4.Mul is {(e:=a*b)}
""")

#Taking Input in Python

fnum=int(input("Enter First Number:"))
snum=int(input("Enter Seconf Number:"))
#sum=a+b
print(sum:=fnum+snum)
