dict1={'cc':10,'aa':20,'dd':30,'bb':10}

dict1.values()

for key,value in dict1.items():
   print(key,value)

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key in sorted(dict1.keys()):
    print(key,dict1[key])

p1={'name':'jack','gender':'male','age':18}
p2={'name':'peter','gender':'female','age':30}
p3={'name':'mark','gender':'male','age':39}

friend=[p1,p2,p3]

for i in friend:
    print(i['name'],i['gender'])


person1={'name':'张三','age':29,'friends':['李四','王五','刘六'],
         'scores':{'语文':66,'数学':89,'英语':70},}
print(person1['scores']['数学'])
j=[]
for i in person1.values():
    j.append(i)
##    print(j)
  
print(j[3]['语文'])


print(set(dict1.values()))
