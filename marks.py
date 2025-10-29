a = int(input("Enter Student 1 marks: "))
b = int(input("Enter Student 2 marks: "))
c = int(input("Enter Student 3 marks: "))
if a > b and a > c:
    print("Student 1 is topper")
elif b > a and b > c:
    print("Student 2 is topper")
else:
    print("Student 3 is topper")
