# Author: Vishal Munic 

CourseOne = input("Enter your course 1 letter grade: ")
OneCredit = float(input("Enter your course 1 credit: "))
if CourseOne == "A" or "a":
  CourseOne = (4.0)
  print("Grade point for course 1 is: 4.0")
elif CourseOne == "A-" or "a-" or "-A" or "-a":
    CourseOne = float(3.67)
    print("Grade point for course 1 is: 3.67")
elif CourseOne == "B+" or "+B" or "+b" or "b+":
    CourseOne = float(3.33)
    print("Grade point for course 1 is: 3.33")
elif CourseOne == "B" or "b":
    print("Grade point for course 1 is: 3.0")
    CourseOne = float(3.0)
elif CourseOne == "-B" or "B-" or "-b" or "b-":
    print ("Grade point for course 1 is: 2.67")
    CourseOne = float(2.67)
elif CourseOne == "C+" or "+C" or "c+" or "+c":
    print("Grade point for course 1 is: 2.33")
    CourseOne = float(2.33)
elif CourseOne == "D" or "d": 
    print("Grade point for course 1 is: 1.0")
    CourseOne = float(1.0)
else:
    print("Grade point for course 1 is: 0")
    CourseOne = float(0)

CourseTwo = input("Enter your course 2 letter grade: ")
TwoCredit = float(input("Enter your course 2 credit: "))
if CourseTwo == "A" or "a":
    print("Grade point for course 2 is: 4.0")
    CourseTwo = (4.0)
elif CourseTwo == "A-" or "a-" or "-A" or "-a":
    print("Grade point for course 2 is: 3.67")
    CourseTwo = float(3.67)
elif CourseTwo == "B+" or "+B" or "+b" or "b+":
    print("Grade point for course 2 is: 3.33")
    CourseTwo = float(3.33)
elif CourseTwo == "B" or "b":
    print("Grade point for course 2 is: 3.0")
    CourseTwo = float(3.0)
elif CourseTwo == "-B" or "B-" or "-b" or "b-":
    print ("Grade point for course 2 is: 2.67")
    CourseTwo = float(2.67)
elif CourseTwo == "C+" or "+C" or "c+" or "+c":
    print("Grade point for course 2 is: 2.33")
    CourseTwo = float(2.33)
elif CourseTwo == "D" or "d": 
    print("Grade point for course 2 is: 1.0")
    CourseTwo = float(1.0)
else:
    print("Grade point for course 2 is: 0")
    CourseTwo = float(0)

CourseThree = input("Enter your course 3 letter grade: ")
ThreeCredit = float(input("Enter your course 3 credit: "))
if CourseThree == "A" or "a":
    print("Grade point for course 3 is: 4.0")
    CourseThree = (4.0)
elif CourseThree == "A-" or "a-" or "-A" or "-a":
    print("Grade point for course 3 is: 3.67")
    CourseThree = float(3.67)
elif CourseThree == "B+" or "+B" or "+b" or "b+":
    print("Grade point for course 3 is: 3.33")
    CourseThree = float(3.33)
elif CourseThree == "B" or "b":
    print("Grade point for course 3 is: 3.0")
    CourseThree = float(3.0)
elif CourseThree == "-B" or "B-" or "-b" or "b-":
    print ("Grade point for course 3 is: 2.67")
    CourseThree = float(2.67)
elif CourseThree == "C+" or "+C" or "c+" or "+c":
    print("Grade point for course 3 is: 2.33")
    CourseThree = float(2.33)
elif CourseThree == "D" or "d": 
    print("Grade point for course 3 is: 1.0")
    CourseThree = float(1.0)
else:
    print("Grade point for course 3 is: 0")
    CourseThree = float(0)


GpaTotal = (((CourseOne * OneCredit) + (CourseTwo * TwoCredit) + (CourseThree * ThreeCredit)) / (OneCredit + TwoCredit + ThreeCredit))

print(f"Your GPA is: {GpaTotal}")