class Sample :
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    
class Child1(Sample):
    def __init__(self, brand, model,year):
        super().__init__(brand, model)
        self.year = year

    def func1(self) : 
        print(f"Brand Name : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
    

c1 = Child1("Mercedes","G-Wagon",2021)
c1.func1()


