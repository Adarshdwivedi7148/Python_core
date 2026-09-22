class Demo:
    a = 4

o = Demo()
print(o.a)  # prints the class attributes because instance atrribute is not present 
o.a = 0   # Instance attribure is set
print(o.a)  # prints the instance attribute because instance attribute is present
print(Demo.a)  # prints the class attribute

