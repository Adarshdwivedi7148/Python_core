words = ["Donkey","bad","ganda"]

with open("filemy.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("filemy.txt","w") as f:
    f.write(content)
