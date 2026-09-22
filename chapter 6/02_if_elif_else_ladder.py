a = int(input("Enter your age : "))

# If elif else ladder

if(a>=18):                  # space is called indentation
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You ar entering 0 which is not a valid age")    

else:
    print("you are below the age of consent")


print("End of the program")