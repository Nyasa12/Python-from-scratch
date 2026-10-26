class Employee:
    salary = 120000
    language = "python"

    def __init__(self, language, name, salary):
            self.name = name
            self.language = language
            self.salary = salary 
            print("this is init constructor method")

    def getinfo(self):
        print(f"My name is {self.name}, this language is {self.language} and the salary is {self.salary}")

harry = Employee("python", "Nyasa", 130000)
harry.getinfo()
