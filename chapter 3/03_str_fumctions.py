# how to use many strings functions 

name = "hello world "

print(len(name))
print(name.endswith("oni"))
print(name.startswith("he"))
print(name.capitalize())              # Capitalizes the first character of the string
print(name.title())              # Capitalizes the first character of each word
print(name.upper())
print(name.lower())
print(name.strip())                   # Removes leading and trailing whitespaces
print(name.count("l"))                # counts the total number of occurrences of any charcter  
print(name.find("world"))                   
print(name.isalnum())                 # Returns 'True' if all charcters are alphanumeric  
print(name.isalpha())                 # Returns 'True' if all charcters are alphabetic 
print(name.isdigit())                 # Returns 'True' if all charcters are digits
print(name.split())

_short = name.replace("world", "python")
print(_short)