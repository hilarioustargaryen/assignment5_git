low = int(input("enter the lower number: "))
high = int(input("enter the higher number: "))
result = 0
for i in range (low,high+1):
  if i%2==1:
   result += i
print(result)
