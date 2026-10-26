class number:
    def __init__ (self, n):
        self.n = n 

    def __add__ (self, num):
        return self.n + num.n
    
n = number(18)
m = number(55)

print(n+m)