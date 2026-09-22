a = 31
b = type(a)  # class <int>
print("Print the value of b :",b)

a = 31.43
b = type(a)  # class <float>
print(b)

a = "31"
b = type(a)  # class <str>
print(b)

a = "31.9"
b = float(a)   # a as a str shown  but the type should be float
s = type(b)
print(s)

int_a = 56
b = str(int_a)
s = type(b)
print(s)

int_b = 98.78
a = int(int_b)
s = type(a)
print(s)