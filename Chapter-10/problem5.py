from random import randint

class train:
    def __init__ (self, trainno, fro, to):
        self.trainno = trainno
        self.fro = fro
        self.to = to
    def book(self):
        print(f"Train is booked in train number:{self.trainno} from {self.fro} to {self.to}")
    def getstatus(self):
        print(f"Train number:{self.trainno} is running on time ")
    def fare(self):
        print(f"ticket fare for train number : {self.trainno} from {self.fro} to {self.to} is {randint(200, 666)}")

t = train(1394902924, "Newyork", "Paris")
t.book()
t.getstatus()
t.fare()
