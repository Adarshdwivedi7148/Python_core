class Employee:            # Employee is class
    age = 23              
    language = "Argenntian"
    salary = 2000000000
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    def greet(self):
        print("Good morning to all")

goi = Employee()          # goi is object
goi.language = "Java"   
goi.getInfo()
goi.greet()
# Employee.getInfo(goi)


