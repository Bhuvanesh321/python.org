class Student:
    mark_bonus = 1.5

    def __init__(self, first,middle, last, marks):
        self.first = first
        self.middle = middle
        self.last = last
        self.marks = marks
        #self.mail = mail

    def mail(self):
        print('{}{}{}@gmail.com'.format(self.middle,self.first,self.last))

    def fullname(self):
        print('{}{}{}' .format(self.first,self.middle, self.last))

    def apply_bonus(self):
        self.marks = int(self.marks*self.mark_bonus)
        print (self.marks)
obj = Student("jamba","lakadi","jarrumitaya",40)
obj.mail()
#print(v)
obj.fullname()
#print(b)
obj.apply_bonus()
#print(a)

