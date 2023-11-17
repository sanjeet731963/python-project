Num=int(input("Enter the number: "))
for i  in range(1,Num+1):
 if Num%i==0:
    [factor].append(i)
print("Factor of {} = {}".format(Num,[factor]))