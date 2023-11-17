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
# def fun1():
#     global a
#     a=6

# def fun2():
#         a=7
# a=5
# print("a intially:",a)
# fun1()
# print("a after fun1:",a)
# fun2()
# print("a after fun2:",a)

#key word arguments
# def sub(a,b):
#     print(a-b)
# sub(5,4)
# sub(a=5,b=4)
# sub(a=4,b=5)
# def welcome(name,message):
#     print(message + name)
# n=input("mame:")
# m=input("message: ")
# welcome(n,m)
# welcome(m,n)
# def welcome(name,message):
#     print(f"{message}  {name}")
# n=input("mame:")
# m=input("message: ")
# welcome(name=n,message=m)
# welcome(message=m,name=n)
# welcome(n,message=m)
# # welcome(m,name=n)
# def pascaltriangle(row):
#     for i in range(0,row):
#         c=1
#         for j in range(1,row-1):
#             print(" ",end=" ")
#     for k in range(0,i+1):
#         print(" ",c,end=" ")
#         c=c*(i-k)//(k+1)
#     print()

# def sum(* args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print("sum:",sum)
    
# sum(1,2,3)
# sum(1,2)




#find largest of n number 
# def ln(*n):
#     l=len(n)
#     num=list(n)
#     for i in range(0,l-1):
#         if num[i]>num[i+1]:
#             num[i+1]=num[i]
#     print("largest:",num[l-1])
# ln(3.6,96,4,13)

#find the si interset;
# si=lambda p, r,t:p*r*t/100
# p=int(input("Enter the principle:"))
# r=int(input("Enter the rate of interst:"))
# t=int(int(input("Enter the time priod:")))
# #p=100
# #r=8
# #t=2
# print("si:",si(p,r,t))

#example of lambed function using if-else
# Max=lambda a, b : a if(a>b) else b
# print(Max(1,19))
# l1=[1,2,3]
# def mul(x):
#     return(x*2)

#result=map(mul,l1)
#print(list(result))
#print(list(map(mul,l1)))#also like this

# print(list(map(lambda x:x*2,l1)))#also like this
# print([x*2 for x in l1])#also like this
#### how to find fectroial by recurgin
# def fac(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return(n*fac(n-1))
# num=int(input("num: "))
# if num<0:
#     print("No factroil")
# else:
#     print("factroial:",fac(num))

    #adding two number using recursion
# def add_numbers(a,b):
#     if b==0:
#         return a    
#     else:
#         return a + add_numbers(1, b-1)
# print(add_numbers(10,5))

#find factroial;

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("Enter the no: "))
# print("factorial: ",factorial(n))

 #adding two no by recursion;
# def add(x,y):
#     if y==0:
#         return x
#     else:
#         return x+add(1,y-1)
# n=int(input("Enter the no: "))
# m=int(input("Enter the no: "))

# print("sum: ",add(n,m,))

#fibbnosirries
# n = 5
# num1 = 0
# num2 = 1
# next_number = num2  
# count = 1
 
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()
############

# def fib(n):
#     if n==1 or n==0:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
    
# num=10
# for i in range(num):
#     print(fib(i))

##########


# def gcd(x,y):
#     if y==0:
#         return x
 # else:
#         return gcd(y,x%y)
# n=12
# m=4
# print(gcd(n,m))

