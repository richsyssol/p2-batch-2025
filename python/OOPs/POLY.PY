class form:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def addmission(self):
        print(self.name)
        print(self.address)
        

class form1:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def addmission(self):
        print(self.name)
        print(self.address)

f1 =form("Uday Ratan Dusane","Jail Road")
f2 =form1("Om Bhujbal","Satpur")
f1.addmission()
f2.addmission()