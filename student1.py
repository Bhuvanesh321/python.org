class Student1:
    def __init__(self,name,marks,mail):
        self.name = name
        self.mail = mail
        self.marks = marks


    def details(self):
        print('{}.{}'.format(self.name,self.marks))

    def mail(self):
        print('{}.{}@gmail.com'.format(self.mail))


obj = Student1("Srini",30)
obj.details()
obj.mail("bh@hmail.com")


