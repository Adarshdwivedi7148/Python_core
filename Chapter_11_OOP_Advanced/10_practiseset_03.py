class Employee:
    salary = 1000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def increment(self,salary):
        self.increment = ((salary/self.salary) -1) * 100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 459.8
print(e.increment)
