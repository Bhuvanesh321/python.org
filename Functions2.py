class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
         return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticObj = StaticClass()
output_add = staticObj.sample_static_method_addition(2,3)
output_mul = staticObj.sample_static_method_multiplication(2,3)
print(output_add, output_mul)

class Computer:
    def config(self):
        print("a9, 20gb, 1TB")
        print("hh,89,us")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
     def config(self):
         print("config is", self.cpu,self.ram)


com1 = Computer('i15',16)
com2 = Computer('abb 3',8)

com1.config()
com2.config()



