sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

avg = (sub1 + sub2 + sub3) / 3

if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and avg >= 40):
    print("Congratulations! You have successfully passed the examination")
else:
    print("Sorry! You could not pass the exam")