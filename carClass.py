class Car:
    def __init__(self,brand,color,isAutomatic,milage,price):
        self.brand = brand
        self.color = color
        self.isAutomatic = isAutomatic
        self.milage = milage
        self.price = price

    def featuresOfCar(self):
        if self.isAutomatic==True:
            print("This car from "+self.brand+". It is "+self.color+" color. "+"The milage of the car is "+str(self.milage)+"kmph. "+"This is a Automatic car. "+"The price of the car is "+str(self.price)+".")
        else:
            print("This car from "+self.brand+". It is "+self.color+" color. "+"The milage of the car is "+str(self.milage)+"kmph. "+"This is a Manual car. "+"The price of the car is "+str(self.price)+".")

car1 = Car("maruti","blue",False,16,600000)
car2 = Car("Tata","White",True,14,1200000)
car1.featuresOfCar()
car2.featuresOfCar()