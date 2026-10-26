marks = {
    "Nyasa" : 100,
    "Kanu" : 99,
    "Anant" :95,
    5 : "twelve"
}

#a.items()
print(marks.items())

#a.keys()
print(marks.keys())

#a.update()
print(marks.update({"Nyasa": 99 , "Renuka" : 57}))

#a.values()
print(marks.values())

#a.get("name")
print(marks.get("Kanu"))


#print(marks["harry2"]) # This will give error as "harry2" key is not present in the dictionary
print(marks.get("harry2")) # This will not give error but will return None


#a.items()
print(marks.items())  

#a.pop("key")
print(marks.pop(5))

#a.popitem()
print(marks.popitem())

#a.clear()
marks.clear()
print(marks)

#a.copy()
new_dict = marks.copy()
print(new_dict)

#a.setdefault(key, default_value)
student = {"name": "Aman"}
student.setdefault("age", 18)
print(student)  
# {'name': 'Aman', 'age': 18}
