data={
    "name" :["John","Sam","Max","Nick","Joe"],
    "dept" :["IT","HR","HR","IT","IT"],
    "salary" :[56000,68000,72000,30000,90000]
    }
sum=0
for i in range(len(data["dept"])):  
    if data["dept"][i]=='IT':
        sum=sum+data["salary"][i]
print(sum)
