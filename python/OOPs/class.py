class Sample :
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    
    def func1(self) : 
        print(f"Brand Name : {self.brand}")
        print(f"Model : {self.model}")
    
s1 = Sample("Mercedes","G-Wagon")
s1.func1()
# s2 = Sample("Ampere","Nexus")
# print(s1.brand)
# print(s1.model)
# print(s2.brand)
# print(s2.model)