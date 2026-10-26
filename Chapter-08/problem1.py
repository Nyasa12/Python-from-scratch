a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
def func1(a, b, c):
   if a>b and a>c:
     print(f"a is the greatest: {a}") 
   elif b>a and b>c:
      print(f"b is the greatest: {b}")
   else:
      print(f"c is the greatest: {c}")
print(func1(a,b,c))  