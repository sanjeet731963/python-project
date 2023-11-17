# def add():
#     a=int(input("a: "))
#     print("sum:",a+5)
# print("Before Function")
# add()
# print("After Function")
# def add(a):
#     print("sub:",a+5)
# def sub(b):
#     print("sub: ", b-5)
# a=int(input("a: "))
# add(a)
# sub(a)
# print("After Function")
# def circle():
#     r=int(input("Enter the radius: "))
#     print("Area of circle: ",3.14*r*r)
# def tringle():
#     b=int(input("Enter the base: "))
#     h=int(input("Enter the hight: "))
#     print("Area of tringle: ", 0.5*b*h) 
# choice=input("Enter or choice c or t: ")
# if choice=="t":
#     tringle()
# elif choice=="c":
#     circle()
# else:
#     print("Enter the valid value: ")
# n="abrakadabra"
# print(n[0])
# l=len(n)
# for i  in range(1,1):
#     flag=0
#     for j in range(0,1):
#         if n[i]==n[j]:
#             flag=1
#         break
#     if flag==0:
#         print(n[i])

#globel and local varible
# def fun1(b):
#     b=b+1
#     print("b inside fun1: ",b)
#     def fun2(a):
#         print("a times 2",a+2)

# a=int(input("enter a: "))
# print("Initial a: ",a)
# fun1(a)
# print("value of a after function call: ",a)