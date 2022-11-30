
class Car():
        def __init__(self,model,marka,year):
            self.model = model
            self.marka = marka
            self.year = year
            self.roads = 0

        def our_cars(self):
            print(self.model,self.marka,self.year)

        def update_roads(self,km):
            if km > self.roads:
                self.roads = km
                print("roads of our",self.model,"is",self.roads)
            else:
                print("tak nelzya")


my_car = Car("Audi", "A8", 2006)
sisters_car = Car("Honda", "Fit", 2008)
my_car.our_cars()
print(my_car.roads)
my_car.update_roads(5000)
print(my_car.roads)
my_car.update_roads(1400)
print(my_car.roads)
print(sisters_car.roads)
sisters_car.update_roads(2000)
print(sisters_car.roads)

class Human():
    def __init__(self,name,age,hobby,year):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.year = year

    def human_charac(self):
        print(self.name,self.age,self.hobby,self.year)

    def check_age(self,this_year):
       print("the age of", self.name , "is",this_year-self.year)

begi = Human("Begi",23,"sport",1999)

begi.human_charac()
begi.check_age(2023)
#
