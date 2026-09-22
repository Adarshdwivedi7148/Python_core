class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def priLanguage(self):
        print(f"Out of all the language here is you language: {self.language}")


class Programmer(Employee,Coder):   # inheritance
     company = "Apple"
     def showLanguage(self):
         print(f"he name is {self.name} and he is good with {self.language} language and my company name is: {self.company} ")
     

#a = Employee()

b = Programmer()

b.name = "Park sino"
#b.language = "Japanese"
b.salary = 3400450

b.show()
b.priLanguage()
b.showLanguage()

