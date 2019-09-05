num1 = input("first number: ")
num2 = input("second number: ")
num3 = input("third number: ")

if num1 < num2 and num1 < num3:
 print("first number is the lowest")
if num2 < num1 and num2 < num3:
 print("second number is the lowest")
if num3 < num1 and num3 < num2:
 print("third number is the lowest")
if num1 == num2 and num2 == num3:
 print("the numbers are equal")