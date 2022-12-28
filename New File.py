class Computer:
    pass

c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

class Computer:
    def __init__(self):
        self.name = "Bhuv"
        self.age = 20

    def update(self):
        self.age = 21

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
   print("They are Same")
else:
    print("they are different")

print(c1.name)
print(c2.name)

