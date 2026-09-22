class Employee:            # Employee is class
    age = 23              
    language = "Argenntian"
    salary = 2000000000
    
    def __init__(self,name,salary,language):   # <-- dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am createing an content")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning to all")

goi = Employee("messi", 140000, "Javascript")    # goi is object
print(goi.name,goi.salary,goi.language)

# goi.getInfo()
# goi.greet()   <--- # Same as work below
# Employee.getInfo(goi)