class calculator:
    def square(self,num):
        return num*num
    def cube(self, num):
        return num*num*num
    def squareroot(self, num):
        return num**1/2
c1 = calculator()
num = int (input("enter the number: "))
print("square of a number", c1.square(num))
print("cube of a number", c1.cube(num))
print("squareroot of a number", c1.squareroot(num))
    