Number = (int(input("Please Enter Your Number: ")))
if Number<0 or Number>100:
   print("Invalid number! Enter a value between 0 to 100")
elif Number>= 0 and Number<=39:
   print("Sorry!,you're fail in this subject\n  Grade point is 0.0\n and,Letter grade is F!")
elif Number >= 40 and Number<=49:
    print("Congratulation!, you successfully  passed\n Grade point 2.0\n Letter grade D")
elif Number>=50 and Number<=59:
    print("Congratulation!,you successfully passed\nGrade point 2.5\nLetter grade C")
elif Number>=60 and Number<=69:
    print("Congratulation!,you successfully passed\nGrade point 3.0\nLetter grade B")
elif Number>=70 and Number<=79:
    print("Congratulation!,you successfully passed\nGrade point 3.5\nLetter grade A")
else:
    print("Congratulation!,you successfully passed\nGrade point 4.0\nLetter grade A+")
