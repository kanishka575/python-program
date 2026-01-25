 #Python Calculator
Operator =input("Enter the Operator(+ - * /):")
Num1 =float(input("Enter the 1st number: "))
Num2 =float(input("Enter the 2nd number: "))

if Operator == "+":
  plus = Num1 + Num2
  print(round(plus,2))
elif Operator == "-":
   minus = Num1 - Num2
   print(round(minus,2))
elif Operator == "*":
   prod = Num1 * Num2
   print(round(prod,2))
elif Operator == "/":
   Divide = Num1 / Num2
   print(round(Divide,2))
else:
    print("It is invalid Operator") 