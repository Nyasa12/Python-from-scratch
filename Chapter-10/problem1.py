class programmer :
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p1 = programmer("Nyasa", 1200000, 251001)
print(p1.company, "\n", p1.name,"\n", p1.salary,"\n", p1.pincode)

p2 = programmer("Anant", 1000000, 251001)
print("\n", p2.company, "\n", p2.name,"\n", p2.salary,"\n", p2.pincode)

p3 = programmer("Rohan", 800000, 251001)
print("\n",p3.company, "\n", p3.name,"\n", p3.salary,"\n", p3.pincode)