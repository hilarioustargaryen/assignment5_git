turns = int(input("how many numbers?:"))
neg=0
pos=0
neg_sum=0
pos_sum=0
for i in range(0,turns,1):
 
 num1 = int(input("pick a number "))
 if num1 < 0:
  
   neg += 1
   neg_sum += num1
 if num1 >= 0:

   pos += 1
   pos_sum += num1
print("you entered ",neg, " negative numbers and " ,pos, "positive numbers")
print("sum of negatives: ", neg_sum," sum of positives: ", pos_sum)
  