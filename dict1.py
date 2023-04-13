data = {
    "names" : ["John", "Mac", "Sam", "Tom"],
    "marks" : [[67,77,87,50], [88,87,98,66], [45,67,54,77], [87,56,67,34]],
    "grade" : ["A","A+","B","B"]
    }

'''
1. Take name of student as input from user
2. Do sum of marks of that student
3. Find percentage of that student
'''

name=input("Enter Student Name: ")
index=data["names"].index(name)
print("Name:",name)
print("Marks :",data["marks"][index])
print("Grade :",data["grade"][index])

sum=0

for i in range (len(data["marks"][index])):
    sum=sum+data["marks"][index][i]

print("Sum of student Marks: ",sum)

per=(sum/400)*100

print("Percentage: ",per,"%")
