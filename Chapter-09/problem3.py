'''n = int(input("enter the number : 6"))
for i in range(1, 11):
    print(f"{i*n}")'''

def generatetable(n):
    table = ""
    for i in range (1, 11):
        table += (f"{n} x {i} = {n*i}\n")

        with open(f"Tables/Table_{n}.txt" , "w") as f:
            f.write(table)

for i in range (2, 21):
    generatetable(i)