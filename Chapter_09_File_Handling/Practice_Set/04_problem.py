word = "Donkey"

with open("filemy.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("filemy.txt","w") as f:
    f.write(contentNew)
