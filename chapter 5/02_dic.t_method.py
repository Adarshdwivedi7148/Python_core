##################### Dictionary is a collection of 'keys-values pairs'  ################################

marks = {
    "Messi" : 100,
    "Lee songki" : 98,
    "Song Kang" : 67,
     "list" : [1,2,4]
}

print(marks,type(marks))
print(marks["Messi"],marks["Lee songki"])


print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Hayyis" : 98})
print(marks)

marks.update({"Messi" : 67})
print(marks)

print(marks.get("Messio"))    # Prints None
print(marks["Messio"])        # Returns an error