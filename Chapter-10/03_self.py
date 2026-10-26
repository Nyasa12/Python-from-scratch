class employee:
    language = "python"
    salary = 1200000

    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")

harry = employee()
harry.greet()
harry.getinfo()
# or
# employee.getinfo(harry)