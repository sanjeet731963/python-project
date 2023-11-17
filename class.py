# class car:
#     pass
# c1=car()
# c2=car()
# c3=car()
# name1=input("name:")
# c1.name=name1
# c1.name="i10"
# c1.brand="Hundai"
# c2.name="harrier"
# c2.brand="tata"
# c3.name="breeza"
# c3.brand="Maruti"
# print("Name of c1 is:",c1.name)
# print("Name of c2 is:",c2.name)
# print("Name of c3 is:",c3.brand)
# #...............
# class student:
#     pass
# s1=student()
# s2=student()
# s1.name="sanjeet"
# s1.regno=12300693
# s2.name="Rajesh"
# s2.regno=112300675
# print("s1 name is:",s1.name)

# class Student:
#     def getdata(self,name,regno):
#         self.n=name
#         self.r=regno
#     def printdata(self):
#         print("Name is:",self.n)
#         print("Reg.Number:",self.r)
# s1=Student()
# s2=Student()
# s3=Student()
# s1.getdata("Sachin",12300693)
# s2.getdata("Maxwell",5678)
# s3.getdata("sanjeet",12300698)
# s1.printdata()
# s2.printdata()
# s3.printdata()
# import math
# result=math.sqrt(9)
# print(result)

# ino=input("Enter the string: ")
# list=[]
# for i in ino:
#     if i.isdigits():
#         list.append(i)
# s=" "
# for i in list:
#     s+=i
# print(s)

#inheritance...........
# class A:
#     def sanjeet(self):
#         print("sanjeet is good boy")
# class B:
#     def rakesh(self):
#         print("rakesh is good boy")
# class C(A,B):
#     def ramesh(self):
#         print("ramesh is not good boy")
# obj=C()
# obj.sanjeet()
# obj.rakesh() 
# obj.ramesh()       
#getter setter..........
# class student:
#     def __init__(self):
#         self.name=" "
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
# obj1=student()
# obj2=student()
# obj1.setname("sanjeet")
# obj2.setname("ramesh")
# x=obj1.getname()
# y=obj2.getname()
# print("name:",x)
# print("name:",y)

# class vehical:
#     def setdetails(self,name,madel):
#         self.n=name
#         self.m=madel
#     def getdeatails(self):
#         print("name:",self.n)
#         print("model:",self.m)
# class bus(vehical):
#     def setbus(self,color):
#         self.c=color
#     def getbus(self):
#         print("color:",self.c)
# b1=bus()
# b1.setdetails("volvo","x11")
# b1.setbus("blue")
# b1.getdeatails()
# b1.getbus()   
 
#Encaplution..............
# class Student:
#     __name="sanjeet"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to my home")
# obj=Student()

#question of class......
# class A():
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         print("name:",self.name)
# class B():
#     def setage(self,age):
#         self.age=age
#     def getage(self):
#         print("age:",self.age)
# class c(A,B):
#     def setaddress(self,address):
#         self.address=address
#     def getaddress(self):
#         print("Address:",self.address)
# obj1=c()
# x=input("Name: ")
# obj1.setname(x) 
# y=input("Age: ")
# obj1.setage(y)
# z=input("Address: ")
# obj1.setaddress(z)
# obj1.getname()
# obj1.getage()
# obj1.getaddress() 


#   POLYMORPHISM........ overloding
# class Ws():
#     def displayinfo(self,name=" "):
#         print("welcome to LPU"+ name)
# obj=Ws()
# obj.displayinfo()
# obj.displayinfo(" sanjeet")

# POLYMORPHISM........ overrading
# class Ws():
#     def displayinfo(self):
#         print("welcome to LPU")
# class IIP(Ws):
#     def displayinfo(self):
#         super().displayinfo()
#         print("welcome to punjab")
# obj=IIP()
# obj.displayinfo()

# overloding question.......
# class Area():
#     def find_area(self,x=None,y=None):
#         if x!=None and y!=None:
#             print("area of rectangle:",x*y)
#         elif x!=None:
#             print("area of squre:",x*x)
#         else:
#             print("Nothing")
# obj=Area()
# obj.find_area()
# obj.find_area(20,4)
# obj.find_area(20)

# Bike rental project..........
class bikeshop():
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes:",self.stock)
    def rentalBike(self,q):
        if q<=0:
            print("Enter the positive value and greater than 0 ")
        elif q>=self.stock:
            print("sory we have only 100 Bikes for rent so plese enter under 100")
        else:
            self.stock=self.stock-q
            print("Total price:",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=bikeshop(100)
    uc=int(input('''
      1 Display Stockes
      2 Rent a Bike
      3 Exit
            '''                             
                 ))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Entetr the qty:......"))
        obj.rentalBike(n)
    else:
        break

##method of over loding not possible in python......
# class greeting:
#     def sayhello(self,name=None,Add=None):
#         if name is not None and Add is not None:
#             print("Hello "+name+Add)
#         elif name is not None and Add is None:
#             print("Hello "+name)
#         else:
#             print("None")
# c1=greeting()
# c1.sayhello("python","23")
# c1.sayhello("python")
# c1.sayhello()

        
# 0ver redding........
# class vechical:
#     def __init__(self,name):
#         self.name=name
#     def getdetails(self):
#         print("name: ",self.name)
# class bus(vechical):
#     def __init__(self,model,color):
#         self.m=model
#         self.color=color
#     def getbus(self):
#         print("color: ",self.color)
#         print("model ",self.m)
# b1=bus("volvo","red")
# b1.getbus()

# class student:
#     name="python"
#     __age=23
#     def getdata(self):
#         print("Name: ",self.name)
#         print("Age: ",self.__age)
# s1=student()
# print("Name: ",s1.name)
# #print("age: ",s1.__age)
# s1.getdata()

        