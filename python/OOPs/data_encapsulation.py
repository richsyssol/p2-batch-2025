class Sample :
    def __init__(self,brand,model): 
        self.__brand = brand
        self.model = model
    
    def func1(self) : 
        print(f"Brand Name : {self.brand}")
        print(f"Model : {self.model}")
    
s1 = Sample("Mercedes","G-Wagon")
s1.func1()