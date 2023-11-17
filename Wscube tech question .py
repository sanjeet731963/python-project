#1. addition of two number:..........
# n1=70
# n2=50
# s=n1+n2
# print("sum of n1 and n2: ",s)


#2. solution 2 (with user ).........
# n1=eval(input("num1: "))
# n2=eval(input("num2: "))
# s=n1+n2
# print("addition of n1 and n2: ",s)

#3print hello world.........
# print("hello world")

#4. how to find squre root....... 
# num1=int(input("enter the number here :"))
# sr=num1**(1/2)
# print("the squre root of the given number is :",sr)

#5. other way to find sr.........
# import math
# num=int(input("Enter the number here: "))
# sr=math.sqrt(num)
# print("The sr of num is: ",sr)

#6. find the area of triangle 
# Hight=float(input("Enter the hight: "))
# Base=float(input("Enter the base: "))
# area=0.5*Base*Hight
# print("area of tringle: ",area)

#7.how to find qurdic eqution...........

# import cmath
# a=int(input("enter the a (a!=0): "))
# b=int(input("enter the b: "))
# c=int(input("enter the c: "))
# d=(b**2)-(4*a*c)
# root1=(-b-cmath.sqrt(d))/(2*a)
# root2=(-b+cmath.sqrt(d))/(2*a)
# print("the roots are",root1,"and",root2)

# 8. change the variable........
# x=21
# y=24
# x,y=y,x
# print("The value of x:",x)
# print("The value of y: ",y)

#9.randome number.......
# import random
# num=random.randint(1,10)
# print(num)

#10.km in miles......
# KM=float(input("km: "))
# miles=(0.621371)*KM
# print(KM,"in miles",miles)

#11.celius in farnihite........
# c=float(input("celsius: "))
# F=(c*9/5)+32
# print(c,"in farnhite",F)

#12.check the number are positive or nagative  or zero...........
# num=int(input("number: "))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("Nagative number")
# else:
#     print("zero")

#13.check  the number are odd or even..........
# num=int(input(" Enter the number:"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

#14.find the year are leap are not......
# year=int(input("Enter the year:"))
# if (year % 400==0)and (year%100==0):
#     print(year," is leap year")
# elif (year%4==0)and (year%100!=0):
#     print(year," is leap year")
# else:
#     print(year," not leap year")

##15.largest number amongst of three number.....
# num1=int(input("Enter the num1: "))
# num2=int(input("Enter the num2: "))
# num3=int(input("Enter the num3: "))
# if num1>num2 and num1>num3:
#     print("largest number are: ",num1)
# elif num2>num1 and num2>num3:
#     print("Largest number are: ",num2)
# else:
#     print("largest number are: ",num3)

#16.check the prime number are not .........

# num=int(input("Enter the num: "))
# if num <= 1:
#     print("it is not prime number: ")
# if num > 1:
#     for i in range (2,num):
#         if num % 2 == 0:
#             print("It is not prime number: ")
#             break
#     else:
#         print("it is prime number: ")

#17.print all prime number in interval...............
# lower=int(input("Enter the  lower number:"))
# upper=int(input("Enter the upper the number: "))
# for num in range (lower,upper+1):
#     if num > 1:
#         for i in range (2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)


#18.find a factroial of a number.........
# num=int(input("Enter the number here: "))
# fact=1
# if num<0:
#     print("factorial dose not exist: ")
# if num==0:
#     print("factroial of 0 is : ",1)
# if num>0:
#     for i in range(1,num+1):
#         fact=fact*i
# print("The factorial of the number is:",fact) 

##19.find factroial using recursion .........
# def fact(a):
#     if a==0:
#         return 1
#     else:
#         return ((a)*fact(a-1))
# num=int(input("Enter the number here: "))
# result=fact(num)
# print("The factroial of the give number: ",result)

##20. disply the muntiplication table..........
# n=int(input("Enter the number: "))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

##21.using while loop..........

# n=int(input("Enter the number here: "))
# i=1
# while i<=10:
#     print(n,"X",i,"=",n*i)
#     i=i+1

##22. print fibonacci sequence ................

# a=0
# b=1
# num=int(input("Enter the number here: "))
# if num==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range (2,num):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# 23.check the number are armstrong are not ..........
# num=int(input("Enter the number here: "))
#order=len(str(num))
# sum=0
# temp=num
# while temp > 0:
#     digit= temp%10
#     cube = digit ** order
#     sum =sum+cube
#     temp//=10
# if sum == num:
#     print("it is an armstrong number ")
# else:
#     print("it is not an armstrong number ")

##24.find the armstrong number in an interval................
# lower=int(input("Enter the lower limit here: "))
# upper=int(input("Enter the upper limit here: "))
# for num in range (lower,upper):
#     order=len(str(num))
#     sum=0
#     temp=num
#     while temp >0:
#         digit =temp%10
#         sum+=digit**order
#         temp//=10
#     if num==sum:
#         print(num)

##25.find the sum of natural number..........
# num=int(input("Enter the number: "))
# if num<0:
#     print("Enter the positive number ")
# else:
#     sum=0
#     while num >0:
#         sum+=num
#         num-=1
#     print(sum)

#26.to display power of 2 using anonmous function.............
# nterms=int(input("Enter  number of terms here:"))
# result=list(map(lambda X: 2**X,range (nterms+1)))
# print(result)
# for i in range(nterms+1):
#     print("the value of 2 raised to power",i,"is",result[i])
#
            