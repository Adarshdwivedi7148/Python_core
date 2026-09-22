class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

pro = Programmer("Messi",1200000, 484001676)      # pro is object
print(pro.name,pro.salary,pro.pin,pro.company)

res = Programmer("Ronaldo",1568800, 987699676)    # res is object
print(res.name,res.salary,res.pin,res.company)