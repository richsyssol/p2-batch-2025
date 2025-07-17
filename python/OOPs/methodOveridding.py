class parent:
    def __init__(self,name):
        self.name=name

    def addmission(self):
        pass
        # print(self.name)        

class child(parent):
    def __init__(self, name,address):
        super().__init__(name)
        self.address = address

    def addmission(self):
        print(self.name)
        print(self.address)


c1 =child("Om Bhujbal","Satpur")
c2 =child("Uday Dusane","JailRoad")
c1.addmission()
c2.addmission()