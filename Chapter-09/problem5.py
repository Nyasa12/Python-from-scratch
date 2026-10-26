word = "donkey"
with open("f.txt","r")as f :
    c = f.read()

content = c.replace("donkey", "######")

with open("f.txt", "w") as f:
   f.write(content)

