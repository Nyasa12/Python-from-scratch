class employee():
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

# e = employee()
# e.a = 45

# e.show()

# class employee():
    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]
e = employee()

e.a = 45
e.name = "Nyasa Tyagi"
# print(e.name)
print(e.fname)
print(e.lname)
print(f"{e.fname} {e.lname}")

e.show()