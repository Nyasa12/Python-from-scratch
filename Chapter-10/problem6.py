from random import randint

class train:
    def __init__ (slf, trainno, fro, to):
        slf.trainno = trainno
        slf.fro = fro
        slf.to = to
    def book(slf):
        print(f"Train is booked in train number:{slf.trainno} from {slf.fro} to {slf.to}")
    def getstatus(slf):
        print(f"Train number:{slf.trainno} is running on time ")
    def fare(slf):
        print(f"ticket fare for train number : {slf.trainno} from {slf.fro} to {slf.to} is {randint(200, 666)}")

t = train(1394902924, "Newyork", "Paris")
t.book()
t.getstatus()
t.fare()
