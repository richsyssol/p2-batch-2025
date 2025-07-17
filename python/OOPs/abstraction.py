from abc import ABC,abstractmethod

class class1(ABC) :
    def __init__(self,num1,name):
        self.num1 =num1
        self.name = name

    @abstractmethod
    def method1(self) :
        pass

class class2(class1) :
    def __init__(self, num1, name):
        super().__init__(num1, name)

    def method1(self) :
        print("Hello World")

c2 = class2(18,"kunal")
c2.method1()