subject1 = int(input("enter the marks of subject 1 out of 100 :"))
subject2 = int(input("enter the marks of subject 2 out of 100 :"))
subject3 = int(input("enter the marks of subject 3 out of 100 :"))

percentage = 100 * (subject1 + subject2 + subject3) / 300

if percentage>=40 and subject1>33 and subject2>33 and subject3>33:
    print("student is passed",percentage)

else:
    print("you are failed",percentage)