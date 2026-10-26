class employee():
    name = "Nyasa"
    salary = 99999999999
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder():
    language = "Python"
    def planguage(self):
        print(f"The language for everyone is {self.language}")
class programmer(employee, coder):
   company = "ITC Infotech"
   def showlanguage(self):
      print(f"The name is {self.name} and he is good with {self.language} language")


a = employee()
b = programmer()

b.show()
b.planguage()
b.showlanguage()