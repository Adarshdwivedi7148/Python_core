name = input("Enter the name: ")
marks = int(input("Enter the marks: "))
phone = int(input("Phone numbers: "))

# Format method
s = ("The name of the student is {}, his marks are {} " 
     "and phone number is {}").format(name,marks,phone)
print(s)

# f-string method
s = (f"The name of the student is {name}, his marks are {marks} " 
     f"and phone number is {phone}")
print(s)