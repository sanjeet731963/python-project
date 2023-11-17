#slicing concatetion in not in repeat 
# str="hello"
# print([1])
# print("e" in str)
# print("u" in str)
# str.upper()

#......
# list1=[1,2,3,4,"python"]
# print("entire list:",list1)
# print("second index:",list[2])
# print("1 -3:",list1[1:3])
# list2=["a","b"]
# print("con:",list1+list2)
# print("Rep:",list1*3)
# list3=list2
# print("list3:",list3)
# list3[0]="c"
# print("list2:",list2)
# print("list3:",list3)
#................
# n=input("input comma separted list:")
# list4=n.split(",")
# print(list4)
# print(type(list4))

#.....
'''
list5=["a","b","c"]
list6=list5
list7=list5.copy()
print("list5:",list5)
print("list7:",list7)
list5[1]="1"
print("list5:",list5)
print("list7:",list7)
print("list6:",list6)
'''
'''
list5=["a","d","r","g","e"]
print(max(list5))
print(min(list5))
print(len(list5))
print("sorted:",sorted(list5))
del list5[2]
print(list5)
Element=list5.pop(1)
print("element:",Element)
list5.clear()
print(list5)
'''
# list5=["a","b","c","d","e"]
# list5.append("f")
# print(list5)
# list6=[1,2]
# list5.append(list6)
# print(list5)
# list5.extend(list6)
# print(list5)
# list5.insert(3,"a")
# print(list5)

#dictionary .py.....
'''
dict1={"name":"sanjeet","age":18,"address":"palra"}
print("dictionary: ",dict1)
print("name is :",dict1["name"])
print("age: ",dict1["age"])
print("address: ",dict1["address"])
str1=input("str1:")
str2=input("str2:")
list1=str1.split(",")
list2=str2.split(",")
d1=dict(zip(list1,list2))
print("D1:",d1)
print(type(d1))
'''
# emp={"name":"python","age":12,"address":"jal"}
# print(emp)
# #emp.clear()
# #print(emp)
# emp1=emp.copy()
# print(emp1)
# sequence=('a','b','c')
# emp2=dict.fromkeys(sequence,11)
# print(emp2)
# print("age:",emp1.get("age"))
# print("keys:",emp1.keys())
# print("values:",emp1.values())
# print("items:",emp1.items())
# emp.update(emp2)
# print("update:",emp1)

#set........
# set1={1,2,3,"a",5}
# print(set1)
# set2=set([1,2,4,3,5])
# print(set2)
# set2.add(8)
# print(set2)
# set2.update([9,10])
# print(set2)
# set2.discard(5)
# set2.remove(1)
# print(set2)
# set3=set1.union(set2)
# print(set3)
# set4=set1.intersection(set2)
# print(set4)
# set5={5,6,7,8,5,6}
# print(set5)
# print(len(set5))
# print(set4.isdisjoint(set5))
# print(set4.issubset(set5))

#list_comprehension
# print([i for i in range(1,11)])
# print([i*2 for i in range(1,11)])
# print([i*2 for i in range(1,11) if i%2==0])
# print([a for a in [1,2,3,4] for b in [2,4,6] if a==b])

#{key:value for (key,value) in iterable}
dict2={i:i*2 for i in range(0,3)}
print(dict2)
list1=[1,2,3]
dict1={key: value for key, in enumerate(list1)}
print(dict1)
list2=['a','b','c']
print(list(enumerate(list2)))
dict3={k:"python" for k in "name"}
print(dict3)