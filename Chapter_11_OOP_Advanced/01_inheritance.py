class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
class Programmer(Employee):
     company = "Apple"
     def showLanguage(self):
         print(f"he name is {self.name} and he is good with {self.language} language")
     

a = Employee()
a.name = "Lee suno"
a.salary = 1200000
a.show()

b = Programmer()
b.name = "Park sino"
b.language = "Japanese"
b.showLanguage()

print(a.name,a.salary,a.company)
print(b.name,b.language,b.company)
