try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")

# Note:--> else is execute only after try excute   