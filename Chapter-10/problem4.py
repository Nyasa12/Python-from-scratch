class calculator:
    def square(self,num):
        return num*num
    def cube(self, num):
        return num*num*num
    def squareroot(self, num):
        return num**1/2
    @staticmethod
    def hello():
        print("hello there!")

c1 = calculator()
c1.hello()
num = int (input("enter the number: "))

print("square of a number", c1.square(num))
print("cube of a number", c1.cube(num))
print("squareroot of a number", c1.squareroot(num))
    