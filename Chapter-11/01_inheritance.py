class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


'''class programmer(employee):
    company = "ITC Tnfotech"
    def show(self):
        print(f"the name is {self.name}")

    def showlanguage(self):
        print(f"the salary is{self.salary}")

a = employee()
b = programmer()
print(a.company, b.company)'''

class programmer(employee):
   company = "ITC Infotech"
   def showlanguage(self):
      print(f"the name is {self.name} and he is good with {self.language} language")


a = employee()
b = programmer()

print(a.company, b.company)