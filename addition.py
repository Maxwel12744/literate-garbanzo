from mymath  import Add,Mul
import mymath
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
except ValueError:
    print("Please enter valid integers.")
    exit()
else:
 print("THE SUM IS:", Add(a, b))
 print("THE PRODUCT IS: ", Mul(a, b))
finally:
    print("Thank you for using the calculator.") 