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