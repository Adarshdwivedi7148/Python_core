# The best way to open and close the file automatically is the with statement.
# Open the file in read mode using 'with', which automaically closes the file.

with open("file.txt","r") as f:
    text = f.read()
    print(text)