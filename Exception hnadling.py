"""try:
    a = int(input())
    b = int(input())
    c = a-b
    print(c)
except:
     print("if {0}/{1} error occured". format(a,b))

finally:
    print("program should excute")"""

class Employees:
    def __init__(self,emp_name,emp_salary,emp_address):
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_address = emp_address
    def details(self):
        try:
            print("emp_name")
            print("emp_salary")
            print("emp_address")
            if(emp_salary>100000):
                  print("salary is more")
            else:
                 print("salary is low")
        except:
            print("salary more than 100000")

