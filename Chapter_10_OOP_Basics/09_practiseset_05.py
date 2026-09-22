from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo 

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is trunning on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(800,3000)}")

t = Train(18322)
t.book("Shahdol", "Indore")
t.getStatus()
t.getFare("Shahdol", "Indore")
