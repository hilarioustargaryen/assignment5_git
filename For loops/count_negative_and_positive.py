turns = int(input("how many numbers?:"))
neg=0
pos=0
for i in range(turns):
 
 num1 = int(input("pick a number "))
 if num1 < 0:
  
   neg += 1
 if num1 >= 0:

   pos += 1
print("you entered ",neg, " negative numbers and " ,pos, "positive numbers")
  